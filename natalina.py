import RPi.GPIO as GPIO
import time

BUZZER = 18
LED = [5,6]

NOTES = {
	"E": 659, "F": 698, "G": 784, "A":880,
	"B": 988, "C": 523, "D":587
}

MELODY = [
	("E", 0.25),("E", 0.25),("E", 0.5),
	("E", 0.25),("E", 0.25),("E", 0.5),
	("E", 0.25),("G", 0.25),("C", 0.25),("D", 0.25),("E", 0.1),
	("F", 0.25),("F", 0.25),("F", 0.25),("F", 0.25),
	("F", 0.25),("E", 0.25),("E", 0.25),("E", 0.25),
	("E", 0.25),("D", 0.25),("D", 0.25),("E", 0.25),("D", 0.5),("G", 0.5)
]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
for pin in LED:
	GPIO.setup(pin, GPIO.OUT)

def play_tone(frequency, duration):
	pwm = GPIO.PWM(BUZZER, frequency)
	pwm.start(50)
	for i in range(2):
		GPIO.output(LED[i % 2], GPIO.HIGH)
		time.sleep(duration / 2)
		GPIO.output(LED[i % 2], GPIO.LOW)
	pwm.stop()

def play_melody():
	for note, duration in MELODY:
		if note == " ":
			time.sleep(duration)
		else:
			play_tone(NOTES[note], duration)
	GPIO.cleanup()

try:
	play_melody()
except KeyboardInterrupt:
	GPIO.cleanup()

