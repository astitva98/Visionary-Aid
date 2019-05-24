import RPi.GPIO as GPIO
import time
import signal
import sys
import threading 
import subprocess
from picamera import PiCamera
from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load("beep-02.mp3")

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)
camera=PiCamera()

flag = 1
Trig = 18
Echo = 24

def playMusic():
    mixer.music.play("beep-02.mp3")
    flag=0



def close(signal, frame):
    print("\nTurning off the system...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
i=1
while True:
    input_state=GPIO.input(6)
    input_state2=GPIO.input(23)
    input_state3=GPIO.input(17)
    if input_state==False:
        print('Button Pressed, waiting for 3 seconds')
        timer = threading.Timer(3.0, playMusic)
        timer.start()
        while(flag):
            continue

        flag=1    

        
    if input_state2==False:
        camera.start_preview()
        sleep(3)
        camera.capture('/home/pi/Desktop/panel1/sample.jpg')
        camera.stop_preview()
        subprocess.call("./automate.sh")
        mixer.music.load("output.wav")
        time=mixer.music.get_length("output.wav")
        mixer.music.play("output.wav")
        if input_state3==false:
            mixer.music.pause()

        if input_state3==false:
            mixer.music.unpause()

        




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



