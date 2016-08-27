from RPi import GPIO
import time
import signal
import sys

def exit_handler(signal, frame):
    print("exit")
    servo.stop()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

pwmPin = 12
dutyFreqHz = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)
servo = GPIO.PWM(pwmPin, dutyFreqHz)

servo.start(0.0)

while True:
    for i in (list(range(10)) + list(reversed(range(10)))):
        dc = 2.5 + (12 - 2.5) * i * 0.111
        servo.ChangeDutyCycle(dc)
        print("dc = %d" % dc)
        time.sleep(0.5)
