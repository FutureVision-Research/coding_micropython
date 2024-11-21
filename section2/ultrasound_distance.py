#This script uses the HC-SR04 ultrasonic sensor to measure distance.
#The result is displayed to the Shell

from machine import Pin
import utime

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

def getdistance(): #This creates a function that communicates with the ultrasonic sensor
    #Send a 5 microsecond (ms) pulse to the Trigger pin to start the measurement 
    trigger.low()  #Ensure the trigger is low before sending the pulse
    utime.sleep_us(2) #Wait for a short period (to ensure no residual pulse)
    trigger.high() #Send a pulse
    utime.sleep_us(5) #Pulse duration
    trigger.low() #End the pulse

 #Measure the pulse width from the Echo pin
while echo.value() == 0:
    signaloff = utime.ticks_us() #Tracks time that passes waiting for sound signal to be received
    while echo.value() == 1:
        signalon = utime.ticks_us() #The Echo pin goes high when the sound signal is received
        timepassed = signalon - signaloff 
        distance = (timepassed * 0.0343) / 2
        print("The distance from object is ",distance,"cm")

while True:
    getdistance()
    utime.sleep(1)
