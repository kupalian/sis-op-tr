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

def __main__():
	if len(sys.argv)==3:
		Posicion=sys.argv[2]
		To=sys.argv[3]
	else:
		print('./aplicacion.py Posicion To')
		print('Ej: ./aplicacion.py 50 0')
		sys.exit(1)
	To=PoscMalla(Posicion,To)
	print(To)
def PoscMalla(Posicion,To):
	T=float(Posicion*0.12)
	if T>To:
		GPIO.output(dire, GPIO.HIGH)
		Tx=T-To
		To=To+Tx
	elif T<To:
		GPIO.output(dire, GPIO.LOW)
		Tx=To-T
		To=To-Tx
	elif T==To:
		Tx=0

motor.ChangeDutyCycle(50)
sleep(Tx)
motor.ChangeDutyCycle(0)
return To
