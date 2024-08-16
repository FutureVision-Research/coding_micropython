# This script causes an external LED to glow when a button is pressed.

import machine
import utime


led_external = machine.Pin(16, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, pull=Pin.NONE) 

while True:
if button.value() == 1:
led_external.value(1)
utime.sleep(2)
led_external.value(0)
