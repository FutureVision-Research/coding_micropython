# Reads the analog input of a potentiometer connected to GP28 and converts that value to a voltage

import machine
import utime
potentiometer = machine.ADC(28)
conversion_factor = 3.3 / (65535)
while True:
voltage = potentiometer.read_u16() * conversion_factor
print(voltage)
utime.sleep(2)
