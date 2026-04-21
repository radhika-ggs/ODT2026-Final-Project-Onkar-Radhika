#import libraries
import json
import math
import os
import random
import time

import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
#set dimentions
WIDTH, HEIGHT = 1500, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⚒  Whack-a-Mole")

#set music and sound volume
MUSIC_VOLUME = 0.5
SFX_VOLUME   = 0.8
#define RGB values for pygame
WHITE    = (255, 255, 255)
YELLOW   = (255, 220,  50)
ORANGE   = (255, 140,  20)
RED      = (220,  50,  50)
GREEN    = ( 80, 200,  80)
LBLUE    = (140, 200, 240)
DIRT     = (101,  67,  33)
SHADOW   = ( 15,  10,   5)
#define font variables
font_big   = pygame.font.SysFont("impact",   80)
font_med   = pygame.font.SysFont("impact",   48)
font_sm    = pygame.font.SysFont("consolas", 28)
font_xs    = pygame.font.SysFont("consolas", 22)
font_key   = pygame.font.SysFont("consolas", 24, bold=True)
font_input = pygame.font.SysFont("consolas", 34, bold=True)
#mole hole grid
COLS, ROWS = 3, 2
CELL_W, CELL_H = 360, 270

GRID_X = (WIDTH  - COLS * CELL_W) // 2
GRID_Y = 185

def cell_center(idx):
    r, c = divmod(idx, COLS)
    return (
        GRID_X + c * CELL_W + CELL_W // 2,
        GRID_Y + r * CELL_H + CELL_H // 2 + 20,
    )

KEY_MAP = {
    pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2,
    pygame.K_4: 3, pygame.K_5: 4, pygame.K_6: 5,
}
KEY_LABELS = ["1", "2", "3", "4", "5", "6"]

HERE = os.path.dirname(os.path.abspath(__file__))
#image loading mech
def asset(name):
    return os.path.join(HERE, name)

def load_img(filename, scale=None, required=True):
    path = asset(filename)
    if not os.path.exists(path):
        if required:
            raise FileNotFoundError(f"Required asset not found: {path}")
        return None
    img = pygame.image.load(path).convert_alpha()
    if scale:
        img = pygame.transform.smoothscale(img, scale)
    return img
#load game assets
IMG_MOLE     = load_img("mole.png",     (120, 120))
IMG_MOLE_HIT = load_img("mole_hit.png", (120, 120))
IMG_HOLE     = load_img("hole.png",     (190,  80))
IMG_BG       = load_img("bg.png",       (WIDTH, HEIGHT))

#music playing for pygame
def play_music(filename, loop=-1):
    path = asset(filename)
    if not os.path.exists(path):
        return
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play(loop)
    except Exception:
        pass

def load_sfx(filename):
    path = asset(filename)
    if not os.path.exists(path):
        return None
    try:
        sfx = pygame.mixer.Sound(path)
        sfx.set_volume(SFX_VOLUME)
        return sfx
    except Exception:
        return None

def play_sfx(sfx):
    if sfx:
        sfx.play()
#music file paths for pygame
SFX_HIT       = load_sfx("sfx_hit.wav")
SFX_MISS      = load_sfx("sfx_miss.wav")
SFX_GAME_OVER = load_sfx("sfx_game_over.wav")
#round specific music array
ROUND_MUSIC = [
    "music_round_1.ogg",
    "music_round_2.ogg",
    "music_round_3.ogg",
    "music_round_4.ogg",
]

#assign local file for leaderboard tracking
SCORE_FILE = asset("whack_leaderboard.json")

def load_leaderboard():
    try:
        with open(SCORE_FILE) as f:
            data = json.load(f)
            if isinstance(data, list): #this is just to make sure that if the file is empty the game doesnt crash
                return data
    except Exception:
        pass
    return []
#write file for leaderboard
def save_leaderboard(board):
    try:
        with open(SCORE_FILE, "w") as f:
            json.dump(board, f, indent=2)
    except Exception:
        pass

def add_to_leaderboard(name, score):
    board = load_leaderboard()
    board.append({"name": name.strip() or "Anonymous", "score": score}) #array format
    board.sort(key=lambda x: x["score"], reverse=True)
    board = board[:10]
    save_leaderboard(board)
    return board

#round settings - durations etc were decided based on playtesting
ROUNDS = [
    {"name": "Round 1 – Sleepy Moles",   "duration": 15, "mole_show": 2.0,  "max_moles": 1, "points": 10},
    {"name": "Round 2 – Waking Up",      "duration": 20, "mole_show": 1.5,  "max_moles": 2, "points": 15},
    {"name": "Round 3 – Getting Cheeky", "duration": 20, "mole_show": 1.1,  "max_moles": 2, "points": 20},
    {"name": "Round 4 – Mole Frenzy",    "duration": 25, "mole_show": 0.8,  "max_moles": 3, "points": 30},
]

#pygame asset drawing
def draw_rounded_rect(surf, color, rect, r=14):
    pygame.draw.rect(surf, color, rect, border_radius=r)

def blit_centered(surf, image, cx, cy):
    surf.blit(image, (cx - image.get_width() // 2, cy - image.get_height() // 2))

def draw_panel(surf, score, round_idx, time_left, combo):
    panel = pygame.Surface((WIDTH, 148), pygame.SRCALPHA)
    panel.fill((20, 14, 8, 215))
    surf.blit(panel, (0, 0))
    pygame.draw.line(surf, ORANGE, (0, 148), (WIDTH, 148), 3)

    title = font_med.render("⚒  WHACK-A-MOLE", True, YELLOW)
    surf.blit(title, (WIDTH // 2 - title.get_width() // 2, 8))

    surf.blit(font_sm.render(f"SCORE: {score}", True, WHITE), (24, 68))

    rnd = font_sm.render(f"ROUND: {round_idx + 1}/{len(ROUNDS)}", True, LBLUE)
    surf.blit(rnd, (WIDTH // 2 - rnd.get_width() // 2, 68))

    timer_color = RED if time_left <= 5 else (ORANGE if time_left <= 10 else GREEN)
    tm = font_sm.render(f"TIME: {time_left}s", True, timer_color)
    surf.blit(tm, (WIDTH - tm.get_width() - 24, 68))

    if combo > 1:
        cb = font_sm.render(f"x{combo} COMBO!", True, ORANGE)
        surf.blit(cb, (WIDTH // 2 - cb.get_width() // 2, 108))

def draw_key_hints(surf):
    for idx in range(6):
        cx, cy = cell_center(idx)
        lbl = font_key.render(KEY_LABELS[idx], True, (220, 220, 180))
        surf.blit(lbl, (cx - lbl.get_width() // 2, cy + 46))

#particle effects- I used an LLM for this part as it is a lot of syntax
class Particle:
    def __init__(self, x, y):
        angle = random.uniform(0, math.tau)
        speed = random.uniform(2, 7)
        self.x, self.y = float(x), float(y)
        self.vx  = math.cos(angle) * speed
        self.vy  = math.sin(angle) * speed
        self.life = random.uniform(0.4, 0.8)
        self.age  = 0.0
        self.col  = random.choice([YELLOW, ORANGE, WHITE, RED])
        self.r    = random.randint(4, 9)

    def update(self, dt):
        self.age += dt
        self.x   += self.vx
        self.y   += self.vy
        self.vy  += 12 * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age / self.life)
        r     = max(1, int(self.r * alpha))
        pygame.draw.circle(surf, self.col, (int(self.x), int(self.y)), r)


class FloatText:
    def __init__(self, x, y, text, color=YELLOW):
        self.x, self.y = float(x), float(y)
        self.text  = text
        self.color = color
        self.life  = 1.0
        self.age   = 0.0

    def update(self, dt):
        self.age += dt
        self.y   -= 60 * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age / self.life)
        lbl = font_med.render(self.text, True,
                              tuple(int(c * alpha) for c in self.color))
        surf.blit(lbl, (int(self.x) - lbl.get_width() // 2, int(self.y)))


particles: list[Particle] = []
floats:    list[FloatText] = []

#screen format and definition
#GAME OVER screen
def name_entry_screen(score):
    play_sfx(SFX_GAME_OVER)
    play_music("music_gameover.ogg")

    clock   = pygame.time.Clock()
    name    = ""
    t       = 0.0
    max_len = 16

    while True:
        dt = clock.tick(60) / 1000
        t += dt

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); raise SystemExit
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    return name if name.strip() else "Anonymous"
                elif ev.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif ev.key == pygame.K_ESCAPE:
                    return "Anonymous"
                elif len(name) < max_len and ev.unicode.isprintable() and ev.unicode:
                    name += ev.unicode
#render all fonts
        screen.blit(IMG_BG, (0, 0))
        ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 160))
        screen.blit(ov, (0, 0))

        title = font_big.render("GAME  OVER", True, RED)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        sc = font_med.render(f"Your score:  {score}", True, WHITE)
        screen.blit(sc, (WIDTH // 2 - sc.get_width() // 2, 240))

        prompt = font_sm.render("Enter your name:", True, YELLOW)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 360))

        box = pygame.Rect(WIDTH // 2 - 220, 410, 440, 58)
        draw_rounded_rect(screen, (40, 30, 18), box, 10)
        pygame.draw.rect(screen, ORANGE, box, 2, border_radius=10)

        display = name + ("|" if int(t * 3) % 2 == 0 else " ")
        screen.blit(font_input.render(display, True, WHITE), (box.x + 14, box.y + 10))

        hint = font_xs.render("ENTER to confirm   ESC to skip", True, (160, 160, 120))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 490))

        pygame.display.flip()

#leaderboard screen
def leaderboard_screen(board, player_score, player_name):
    clock = pygame.time.Clock()
    t     = 0.0

    while True:
        dt = clock.tick(60) / 1000
        t += dt

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); raise SystemExit
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:  return True
                if ev.key == pygame.K_ESCAPE:  return False

        screen.blit(IMG_BG, (0, 0))
        ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 150))
        screen.blit(ov, (0, 0))

        title = font_big.render("LEADERBOARD", True, YELLOW)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        hdr = font_sm.render(f"{'#':<4}  {'NAME':<18}{'SCORE':>6}", True, ORANGE)
        screen.blit(hdr, (WIDTH // 2 - hdr.get_width() // 2, 160))
        pygame.draw.line(screen, ORANGE,
                         (WIDTH // 2 - 240, 196), (WIDTH // 2 + 240, 196), 2)

        position = ["1", "2", "3", "  4", "  5"]
        for rank, entry in enumerate(board[:5]):
            is_me = (entry["name"] == player_name and entry["score"] == player_score)
            row_y = 210 + rank * 76

            if is_me:
                pulse  = int(40 + 20 * math.sin(t * 5))
                hl_box = pygame.Rect(WIDTH // 2 - 245, row_y - 8, 490, 60)
                draw_rounded_rect(screen, (pulse, pulse // 2, 0), hl_box, 10)
                pygame.draw.rect(screen, ORANGE, hl_box, 2, border_radius=10)

            row = font_sm.render(
                f"{position[rank]}  {entry['name'][:16]:<16}  {entry['score']:>6}",
                True, YELLOW if is_me else WHITE #highlight current player score
            )
            screen.blit(row, (WIDTH // 2 - row.get_width() // 2, row_y))

        player_rank = next(
            (i + 1 for i, e in enumerate(board)
             if e["name"] == player_name and e["score"] == player_score),
            None
        )
        if player_rank and player_rank > 5:
            sep_y = 210 + 5 * 76 + 10
            pygame.draw.line(screen, (100, 80, 40),
                             (WIDTH // 2 - 240, sep_y), (WIDTH // 2 + 240, sep_y), 1)
            your = font_sm.render(
                f"  {player_rank}   {player_name[:16]:<16}  {player_score:>6}  ← you",
                True, ORANGE
            )
            screen.blit(your, (WIDTH // 2 - your.get_width() // 2, sep_y + 12))
#we added this grading system to increase competition
        grade = (
            "S – LEGENDARY!" if player_score >= 500 else
            "A – Amazing!"   if player_score >= 350 else
            "B – Nice work!" if player_score >= 200 else
            "C – Keep at it!" if player_score >= 100 else
            "D – Try again!"
        )
        gr = font_med.render(grade, True, LBLUE)
        screen.blit(gr, (WIDTH // 2 - gr.get_width() // 2, 660))

        pulse2 = int(180 + 75 * math.sin(t * 3))
        en = font_sm.render("ENTER – Play Again    ESC – Quit", True, (pulse2, pulse2, 80))
        screen.blit(en, (WIDTH // 2 - en.get_width() // 2, 760))

        pygame.display.flip()


def start_screen():
    play_music("music_start.ogg")

    clock = pygame.time.Clock()
    t     = 0.0
    board = load_leaderboard()

    while True:
        dt = clock.tick(60) / 1000
        t += dt

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); raise SystemExit
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN: return
                if ev.key == pygame.K_ESCAPE:
                    pygame.quit(); raise SystemExit

        screen.blit(IMG_BG, (0, 0))

        scale  = 1 + 0.04 * math.sin(t * 3)
        raw    = font_big.render("WHACK-A-MOLE", True, YELLOW)
        scaled = pygame.transform.smoothscale(
            raw, (int(raw.get_width() * scale), int(raw.get_height() * scale))
        )
        screen.blit(scaled, (WIDTH // 2 - scaled.get_width() // 2, 36))

        by = int(240 + math.sin(t * 2.5) * 20)
        blit_centered(screen, IMG_HOLE, WIDTH // 2, by + 68)
        blit_centered(screen, IMG_MOLE, WIDTH // 2, by)

        sq = 48
        gx = WIDTH // 2 - (3 * (sq + 8)) // 2
        gy = 420
        for i in range(6):
            r, c = divmod(i, 3)
            rx = gx + c * (sq + 8)
            ry = gy + r * (sq + 8)
            draw_rounded_rect(screen, DIRT, (rx, ry, sq, sq), 6)
            lbl = font_key.render(str(i + 1), True, YELLOW)
            screen.blit(lbl, (rx + sq // 2 - lbl.get_width()  // 2,
                               ry + sq // 2 - lbl.get_height() // 2))

        hint = font_sm.render("Keys  1–6  map to the 2×3 grid", True, LBLUE)
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 550))

        if board:
            lb_title = font_xs.render("TOP SCORES", True, ORANGE)
            screen.blit(lb_title, (WIDTH // 2 - lb_title.get_width() // 2, 610))
            for i, entry in enumerate(board[:3]):
                row = font_xs.render(
                    f"{i+1}. {entry['name'][:14]:<14} {entry['score']}",
                    True, WHITE
                )
                screen.blit(row, (WIDTH // 2 - row.get_width() // 2, 640 + i * 34))

        pulse = int(200 + 55 * math.sin(t * 4))
        pe = font_sm.render("PRESS  ENTER  TO  START", True, (pulse, pulse, 80))
        screen.blit(pe, (WIDTH // 2 - pe.get_width() // 2, 880))

        pygame.display.flip()

#round transition screen
def round_transition(round_idx, score):
    play_music(ROUND_MUSIC[round_idx])

    clock = pygame.time.Clock()
    t     = 0.0
    cfg   = ROUNDS[round_idx]

    while True:
        dt = clock.tick(60) / 1000
        t += dt

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); raise SystemExit
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return

        if t > 2.8:
            return

        screen.blit(IMG_BG, (0, 0))

        spacing = 265
        start_x = WIDTH // 2 - spacing
        for xi in range(3):
            bx = start_x + xi * spacing
            by = int(430 + math.sin(t * 3 + xi * 1.2) * 22)
            blit_centered(screen, IMG_HOLE, bx, by + 68)
            blit_centered(screen, IMG_MOLE, bx, by)

        rn = font_big.render(f"ROUND  {round_idx + 1}", True, YELLOW)
        screen.blit(rn, (WIDTH // 2 - rn.get_width() // 2, 90))

        nm = font_sm.render(cfg["name"], True, ORANGE)
        screen.blit(nm, (WIDTH // 2 - nm.get_width() // 2, 200))

        sc = font_sm.render(f"Score so far: {score}", True, WHITE)
        screen.blit(sc, (WIDTH // 2 - sc.get_width() // 2, 256))

        info = (f"Mole time: {cfg['mole_show']:.2f}s   "
                f"Max moles: {cfg['max_moles']}   "
                f"Points: {cfg['points']}")
        in_txt = font_xs.render(info, True, LBLUE)
        screen.blit(in_txt, (WIDTH // 2 - in_txt.get_width() // 2, 300))

        cd = max(0, 3 - int(t))
        cd_txt = font_big.render(str(cd) if cd > 0 else "GO!", True, GREEN)
        screen.blit(cd_txt, (WIDTH // 2 - cd_txt.get_width() // 2, 590))

        pygame.display.flip()

#base game screen
def play_round(round_idx, score):
    cfg           = ROUNDS[round_idx]
    mole_show     = cfg["mole_show"]
    max_moles     = cfg["max_moles"]
    pts           = cfg["points"]

    moles         = {}
    whack_anim    = {}
    next_mole_t   = 0.0
    mole_interval = mole_show * 0.8
    combo         = 0
    last_whack    = 0.0

    global particles, floats
    particles, floats = [], []

    clock = pygame.time.Clock()
    start = time.time()

    while True:
        dt        = clock.tick(60) / 1000
        now       = time.time()
        elapsed   = now - start
        time_left = max(0, int(cfg["duration"] - elapsed))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); raise SystemExit

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return score, False

                if ev.key in KEY_MAP:
                    idx = KEY_MAP[ev.key]
                    cx, cy = cell_center(idx)

                    if idx in moles and now < moles[idx]:
                        del moles[idx]
                        whack_anim[idx]  = now + 0.28

                        combo   = combo + 1 if (now - last_whack < 1.5) else 1
                        last_whack = now
                        earned  = pts + (combo - 1) * 5
                        score  += earned

                        play_sfx(SFX_HIT)
                        for _ in range(20):
                            particles.append(Particle(cx, cy))
                        label = f"+{earned}" + ("  COMBO!" if combo > 1 else "")
                        floats.append(FloatText(cx, cy - 50, label))
                    else:
                        combo = 0
                        play_sfx(SFX_MISS)
                        floats.append(FloatText(cx, cy - 20, "MISS!", RED))

        if now >= next_mole_t and len(moles) < max_moles:
            available = [i for i in range(6) if i not in moles]
            if available:
                idx = random.choice(available)
                moles[idx]  = now + mole_show
                next_mole_t = now + mole_interval * random.uniform(0.7, 1.3)

        moles     = {i: t for i, t in moles.items() if now < t}
        particles = [p for p in particles if p.age < p.life]
        floats    = [f for f in floats    if f.age < f.life]
        for p in particles: p.update(dt)
        for f in floats:    f.update(dt)

        screen.blit(IMG_BG, (0, 0))
        draw_panel(screen, score, round_idx, time_left, combo)

        for idx in range(6):
            cx, cy = cell_center(idx)
            blit_centered(screen, IMG_HOLE, cx, cy + 50)

        for idx in range(6):
            cx, cy = cell_center(idx)
            if idx in whack_anim and now < whack_anim[idx]:
                blit_centered(screen, IMG_MOLE_HIT, cx, cy - 15)
            elif idx in moles:
                pct = (moles[idx] - now) / mole_show
                bob = int(10 * math.sin((1 - pct) * math.pi))
                blit_centered(screen, IMG_MOLE, cx, cy - 14 - bob)


        draw_key_hints(screen)
        for p in particles: p.draw(screen)
        for f in floats:    f.draw(screen)

        rn = font_xs.render(cfg["name"], True, (180, 140, 80))
        screen.blit(rn, (WIDTH // 2 - rn.get_width() // 2, 152))

        pygame.display.flip()

        if time_left == 0:
            return score, True


def main():
    while True:
        start_screen()

        score = 0
        for round_idx in range(len(ROUNDS)):
            round_transition(round_idx, score)
            score, cont = play_round(round_idx, score)
            if not cont:
                break

        player_name = name_entry_screen(score)
        board       = add_to_leaderboard(player_name, score)

        if not leaderboard_screen(board, score, player_name):
            break

    pygame.quit()

#running
if __name__ == "__main__":
    main()