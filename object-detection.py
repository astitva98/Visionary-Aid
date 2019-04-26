import RPi.GPIO as GPIO
import time
import signal
import sys

from pygame import mixer
mixer.init()
mixer.music.load("beep-02.mp3")

# For Using Raspberry Pi's pin numbers
GPIO.setmode(GPIO.BCM)

Trig = 17
Echo = 24

def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

while True:
    # set Trigger to HIGH
    GPIO.output(Trig, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(Trig, False)

    startTime = time.time()
    stopTime = time.time()

    # save start time
    while 0 == GPIO.input(Echo):
        startTime = time.time()

    # save time of arrival
    while 1 == GPIO.input(Echo):
        stopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = stopTime - startTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    if distance < 50 :
        mixer.music.play(2)
        
    print ("Distance: %.1f cm" % distance)
    time.sleep(1)
