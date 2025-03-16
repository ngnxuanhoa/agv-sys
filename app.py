from flask import Flask, render_template, Response, request
import cv2
import RPi.GPIO as GPIO

app = Flask(__name__)

# Cấu hình GPIO
motor1_pwm = 18
motor1_in1 = 23
motor1_in2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pwm, GPIO.OUT)
GPIO.setup(motor1_in1, GPIO.OUT)
GPIO.setup(motor1_in2, GPIO.OUT)

pwm = GPIO.PWM(motor1_pwm, 1000)
pwm.start(0)

# Hàm điều khiển động cơ
def move(command):
    if command == "forward":
        GPIO.output(motor1_in1, GPIO.HIGH)
        GPIO.output(motor1_in2, GPIO.LOW)
        pwm.ChangeDutyCycle(50)
    elif command == "backward":
        GPIO.output(motor1_in1, GPIO.LOW)
        GPIO.output(motor1_in2, GPIO.HIGH)
        pwm.ChangeDutyCycle(50)
    elif command == "stop":
        pwm.ChangeDutyCycle(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['GET'])
def control():
    cmd = request.args.get('cmd')
    move(cmd)
    return "OK"

# Xử lý video từ camera
def gen():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame
'
               b'Content-Type: image/jpeg

' + buffer.tobytes() + b'
')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
