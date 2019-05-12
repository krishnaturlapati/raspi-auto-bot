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

@app.route("/<deviceName>/<action>")
def action(deviceName, action):

    def change_direction(n1 ,n2):
        pin1.ChangeDutyCycle(n1)
        pin2.ChangeDutyCycle(n2)

    if deviceName == 'servo' and action == 'forward':
       change_direction(10,2.5)
    if deviceName == 'servo' and action == 'reverse':
       change_direction(2.5,10)
    if deviceName == 'servo' and action == 'right':
       change_direction(0,2.5)
    if deviceName == 'servo' and action == 'left':
       change_direction(2.5,0)
    if deviceName == 'servo' and action == 'stop':
       change_direction(0,0)

    templateData  = {
     'servo_status' : action
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

