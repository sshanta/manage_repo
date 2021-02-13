import time             # image time library
import RPi.GPIO as GPIO # import python package for GPIO's
GPIO.setmode(GPIO.BCM) # Sets Pin Configuration
GPIO.setup(2,GPIO.OUT) # Sets Output Pin
LED = GPIO.PWM(2, 50)
LED.start(0)
try:
	while(1):
		GPIO.output(2,GPIO.HIGH) # Logic 1 on Pin
		time.sleep(1)
		GPIO.output(2,GPIO.LOW) # Logic 0 on Pin
		time.sleep(1)
except KeyboardInterrupt:
	pass
p.stop()
GPIO.cleanup()  #leaving GPIO's at their default values
