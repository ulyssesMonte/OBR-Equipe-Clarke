#!/usr/bin/env python3

from time import sleep
from ev3dev.ev3 import LargeMotor, GyroSensor, UltrasonicSensor
from os import system

system('setfont Lat15-TerminusBold14')

l = LargeMotor('outB')
r = LargeMotor('outA')
gyro = GyroSensor('in3')
sonic = UltrasonicSensor('in4')

def girar(graus):
	pos0 = gyro.value()
	if(graus > 0):
		while gyro.value() < pos0 + graus:
			l.run_forever(speed_sp=-500)
			r.run_forever(speed_sp=250)
	else:
		while gyro.value() > pos0 + graus:
			l.run_forever(speed_sp=250)
			r.run_forever(speed_sp=-500)

	l.stop()
	r.stop()

def andarEmGraus(graus):
	l.run_to_rel_pos(position_sp=graus, speed_sp=900, stop_action="hold")
	r.run_to_rel_pos(position_sp=graus, speed_sp=900, stop_action="hold")

def desviar():
	pos0 = gyro.value()

	girar(82)
	sleep(0.1)
	andarEmGraus(-400)
	sleep(1)

	girar(-82)
	sleep(0.1)
	andarEmGraus(-1000)
	sleep(2)

	girar(-82)
	sleep(0.1)
	andarEmGraus(-500)
	sleep(1.5)

	girar(82)
	sleep(0.1)

	andarEmGraus(200)
	sleep(0.3)
while True:
	print(sonic.value())
	if(sonic.value() < 70):
		desviar()
		break