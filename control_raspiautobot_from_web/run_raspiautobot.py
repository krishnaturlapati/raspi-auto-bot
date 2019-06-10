import datetime
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template


# Flask setup
app = Flask(__name__)

# GPIO setup
servo_pin1 = 17
servo_pin2 = 27


GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
pin1 = GPIO.PWM(int(servo_pin1), 50) # set GPIO pin for PWM with 50Hz
pin1.start(0) 

GPIO.setup(servo_pin2, GPIO.OUT)
pin2 = GPIO.PWM(int(servo_pin2), 50)
pin2.start(0)



# servo helper function
def control_servo(action):
    def change_direction(n1, n2):
        pin1.ChangeDutyCycle(n1)
        pin2.ChangeDutyCycle(n2)
    if action == 'forward':
        change_direction(10, 2.5)
    if action == 'reverse':
        change_direction(2.5, 10)
    if action == 'right':
       change_direction(2.5, 0)
    if action == 'stop':
       change_direction(0,0)

# dc motor helper function
def control_dcmotor(action):
    pass


@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'Testing Servo',
      'time' : timeString,
      'servo_status': 'waiting'
    }
    return render_template('index.html', **templateData)

@app.route("/<device_name>/<action>")
def action(device_name, action):
    if device_name == 'servo':
        control_servo(action)
    if device_name == 'dcmotor':
       control_dcmotor(action)

    templateData  = {
      device_name : action
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

