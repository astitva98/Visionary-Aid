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
GPIO.setup(22,GPIO.OUT)
GPIO.setup(5, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)
camera=PiCamera()

flag = 1
Trig = 18
Echo = 24

def playMusic():
    mixer.music.load("beep-02.mp3")
    mixer.music.play(2)
    flag = 0

def camer():
    GPIO.output(22, 1)
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/Visionary-Aid/sample1.jpg')
    GPIO.output(22, 0)
    camera.stop_preview()
    subprocess.call("./automate.sh")

def close(signal, frame):
    print("\nTurning off the system...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
i=1
stpa = 0
while True:
    input_state=GPIO.input(12)
    input_state2=GPIO.input(23)
    input_state3=GPIO.input(13)
    input_state4=GPIO.input(5)
    input_state5=GPIO.input(6)
    if input_state==False:
        print('Button Pressed, waiting for 3 seconds')
        timer = threading.Timer(3.0, playMusic)
        timer.start()
        while(flag):
            continue

        flag=1    

    flagg1 = 1

    if input_state2==False:
        mixer.music.load("ooo.mp3")
        mixer.music.play(0)
        while(mixer.music.get_busy()):
            input_state=GPIO.input(12)
            input_state2=GPIO.input(23)
            input_state3=GPIO.input(13)
            input_state4=GPIO.input(5)
            input_state5=GPIO.input(6)
            if input_state3==False: 
                if stpa == 0:
                    mixer.music.pause()
                    print("Pause")
                    stpa = 1
                else:
                    mixer.music.unpause()
                    print("Play")
                    stpa = 0
                time.sleep(0.1)
            if input_state4 == False:
                print("Forward")
                mixer.music.set_pos(10)
                time.sleep(0.1)
            if input_state5 == False:
                print("Rewind")
                mixer.music.set_pos(-15)
                time.sleep(0.1)
        
        mixer.music.load("beep-02.mp3")

        
    if mixer.music.get_busy() == False:
        flagg1=1

    if flagg1 == 0: 
        continue



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



