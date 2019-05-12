import RPi.GPIO as GPIO
import time
import sys

heart_beat = 26
servo_pin1 = 17
servo_pin2 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin1, GPIO.OUT)
pin1 = GPIO.PWM(int(servo_pin1), 50) # set GPIO pin for PWM with 50Hz
pin1.start(2.5) # Initializatio

GPIO.setup(servo_pin2, GPIO.OUT)
pin2 = GPIO.PWM(int(servo_pin2), 50)
pin2.start(2.5)

def change_direction(n1 ,n2):
    pin1.ChangeDutyCycle(n1)
    pin2.ChangeDutyCycle(n2)


def main():
    pins = [26, 17, 27]
    try:
      while True:
          # move forward
          change_direction(10,2.5)
          time.sleep(1)
          # move right
          change_direction(0,2.5)
          time.sleep(1)
          # move reverse
          #change_direction(2.5, 10)
          #time.sleep(1)
          # move left
          change_direction(10, 2.5)
          time.sleep(1)
          # move forward
          change_direction(2.5, 0)
          time.sleep(1)
    except KeyboardInterrupt:
        pin1.stop()
        pin2.stop()
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


if __name__=="__main__":
    main()
