#!/usr/bin/python2
#AndresOrdMar3
from time import sleep
import RPi.GPIO as GPIO
import sys

enable=16
step=20
dire=21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(enable,GPIO.OUT)
GPIO.setup(dire,GPIO.OUT)
GPIO.setup(step,GPIO.OUT)

motor=GPIO.PWM(step,1600)
motor.start(0)
Tx=float(0)
To=float(0)

if len(sys.argv)==3:
	T=int(sys.argv[1])*0.12
	To=int(sys.argv[2])*0.12

	print('Posicion Deseada={} Posicion Actual={}'.format(sys.argv[1],sys.argv[2]))

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

	print('Tiempo de Espera:{0:2f}s '.format(Tx))

	motor.ChangeDutyCycle(50)
	sleep(Tx)
	motor.ChangeDutyCycle(0)
	print('Posicion Final={0:3f}'.format(To/0.12))
else:
	print('Error de syntaxis. Escriba: ./aplicacion.py Posicion_Deseada  Posicion_Actual')
	print('Ejemplo: ./aplicacion.py 50 0')
