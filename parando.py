import RPI.GPIO as GPIO

BUZZER = 18
LED = [5, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
for pin in LED:
	GPIO.setup(pin, GPIO.OUT)

GPIO.output(BUZZER, GPIO.LOW)
for pin in LED:
	GPIO.output(pin, GPIO.LOW)

GPIO.clenup()
