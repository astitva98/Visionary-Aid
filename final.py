import RPi.GPIO as GPIO
import time
import signal
import sys
from picamera import PiCamera
from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load("beep-02.mp3")

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
camera=PiCamera()


Trig = 18
Echo = 24

def close(signal, frame):
    print("\nTurning off the system...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
i=1
while True:
    input_state=GPIO.input(23)
    input_state2=GPIO.input(4)
    if input_state==False:
        print('Button Pressed')
        mixer.music.play()
        
    if input_state2==False:
        camera.start_preview()
        sleep(3)
        camera.stop_preview()
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)

    startTime = time.time()
    stopTime = time.time()

    while 0 == GPIO.input(Echo):
        startTime = time.time()

    while 1 == GPIO.input(Echo):
        stopTime = time.time()

    TimeElapsed = stopTime - startTime
    distance = (TimeElapsed * 34300) / 2
    
    if distance < 50 :
        mixer.music.play()
        print ("Distance: %.1f cm" % distance)
        time.sleep(0.5)
        
    
    time.sleep(0.01)



