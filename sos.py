import RPi.GPIO as GPIO
import time

from pygame import mixer
mixer.init()
mixer.music.load("beep-02.mp3")

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    input_state=GPIO.input(18)
    if input_state==False:
        print('Button Pressed')
        mixer.music.play()
        time.sleep(1)


        


