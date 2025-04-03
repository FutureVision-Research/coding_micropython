# This script uses the library neopixel to cycle five LEDs through the range of available colors.
# Keep in mind: We are using the neopixel library included with MicroPython, which is a minimal, low-level library developed by the MicroPython team.
# Adafruit provides a more feature-rich NeoPixel library for their own fork of MicroPython, called CircuitPython.

import machine
import neopixel
import time

# === Configuration ===
NUM_LEDS = 5
LED_PIN = 15
DELAY = 0.1
BRIGHTNESS = 0.3  # Set brightness (0.0 to 1.0)

# === Setup ===
pin = machine.Pin(LED_PIN)
np = neopixel.NeoPixel(pin, NUM_LEDS)

# === Color wheel helper ===
def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# === Brightness scaling helper ===
def scale_color(color, brightness):
    return tuple(int(c * brightness) for c in color)

# === Main loop ===
offset = 0
try:
    while True:
        for i in range(NUM_LEDS):
            color_index = (offset + i * 30) % 256
            raw_color = wheel(color_index)
            np[i] = scale_color(raw_color, BRIGHTNESS)
        np.write()
        offset = (offset + 5) % 256
        time.sleep(DELAY)

except KeyboardInterrupt: #executes the following code block if user breaks out of the program
    for i in range(NUM_LEDS):
            np[i] = (0, 0, 0) #Sets each LED to "no color"
    np.write() # Sends color setting to LEDs
    print("All LEDs are off. Exiting program.")
