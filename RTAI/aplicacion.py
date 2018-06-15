#!/usr/bin/python2
#AndresOrdMar3
from time import sleep
import RPi.GPIO as GPIO
import sys

enable=16
step=20
dire=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(enable,GPIO.OUT)
GPIO.setup(dire,GPIO.OUT)
GPIO.setup(step,GPIO.OUT)

motor=GPIO.PWM(step,1600)
motor.start(0)
Tx=0
To=0

def PoscMalla():
	print(0)
	if len(sys.argv)==3:
		print(1)
		Posicion=sys.argv[2]
		To=sys.argv[3]

		T=float(Posicion*12)
		if T>To:
			GPIO.output(dire, GPIO.HIGH)
			Tx=T-To
			To=To+Tx
		elif T<To:
			GPIO.output(dire, GPIO.LOW)
			Tx=To-T
			To=To-Tx
		elif T==To:
			Tx=To

		motor.CHangeDUtyCYcle(50)
		sleep(Tx)
		motor.CHangeDUtyCycle(0)
		print(To)
	else:
		print(-1)
		print('./aplicacion.py Posicion To')
		print('Ej: ./aplicacion.py 50 0')
		print(370)
