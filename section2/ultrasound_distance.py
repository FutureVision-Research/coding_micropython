# This script use a HC-SR04 to measure distance. The measurement is displayed in the Shell.

from machine import Pin #Pin allows us to communicate with GPIO pins
import utime #Used to introduce a delay into our script
 
# Set up GPIO pins for communication with the sensor
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

while True:
    # Set the trigger to low so no sound is being transmitted.
    trigger.low()
    utime.sleep_us(2)
    # Send sound for 5 µs
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
   
    # Echo pin on the sensor is high when sound is heard and low when there is no sound.
    # Echo pin will be low after untill the pulse hits an object and returns.
    # Echo will go high after pulse is detected.
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
   
    # The time between signaloff and signalon gives us the travel time of the pulse.
    timepassed = signalon - signaloff
   
    # We only need to know the travel time to the object, so the value is divided by two.
    # The value 0.0343 is based on the speed of sound through air.
    distance_cm = (timepassed * 0.0343) / 2
   
    # Display the measurement in centimeters and inches
    print("The distance from object is ",distance_cm,"cm")
    print("The distance from object is ",distance_cm/2.54, "in")
    utime.sleep(2) # Slight delay to read the measurement before restarting the loop