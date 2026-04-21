from machine import TouchPad, Pin
import time

# --- Setup ---
touch_pins = [32, 4, 14, 12, 13, 33]
touchpads = [TouchPad(Pin(p)) for p in touch_pins]
while True:
    not_touched = []
    touched = []
    thresholds = []

    # --- Step 1: NOT TOUCHED ---
    print("⚠️ Don't touch ANY sensors...")
    time.sleep(3)

    for i, t in enumerate(touchpads):
        vals = []
        for _ in range(50):
            vals.append(t.read())
            time.sleep(0.02)
        
        avg = sum(vals) // len(vals)
        not_touched.append(avg)
        print(f"Pin {touch_pins[i]} not touched avg: {avg}")

    # --- Step 2: TOUCHED (one by one) ---
    print("\nNow we go pin by pin. Touch ONLY the requested pin.\n")

    for i, t in enumerate(touchpads):
        print(f" Touch pin {touch_pins[i]} NOW")
        time.sleep(2)

        vals = []
        for _ in range(50):
            vals.append(t.read())
            time.sleep(0.02)

        avg = sum(vals) // len(vals)
        touched.append(avg)

        print(f"Pin {touch_pins[i]} touched avg: {avg}\n")

    # --- Step 3: Compute thresholds ---
    print("Calculating thresholds...\n")

    for i in range(len(touchpads)):
        th = (not_touched[i] + touched[i]) // 2
        thresholds.append(th)
        touchpads[i].config(th)

        print(f"Pin {touch_pins[i]} → Threshold: {th}")

    print("\nCalibration complete.\n")

    # --- Step 4: Live monitoring ---

      

