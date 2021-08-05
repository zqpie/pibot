from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
import picar
import os
import curses # keyboard inputs






#    controls for the pibot software are as follows



#  w speeds up the rear wheels


#  s puts the car in reverse 


#  a and d turn the front wheels


#  and the arrow keys control the cameras servos


#  e sets the front wheels to the center


#  r sets the wheels to a resting speed


#  and finally t resets all the wheels and servos to the center





















	# inputs in this file are as follows:

	# you can activate and deactivate "drift mode" witch is where full speed moter motion can be instantly swaped for full speed backwards motion, and the tires drift.

	# next you can tweak the servos resting angle in the reset servos section.

	#also you can modify the controlls.




picar.setup()
os.system('clear')
							# misc setup
bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)
picar.setup()
screen = curses.initscr()
curses.noecho() # makes keystroks not displayed
curses.cbreak() # no clue
screen.keypad(True)









#use this tweak to change the moters middle potition ######
wheel = 90					   	  # servo                                  #
speed = 0					  	  # middle                                ##
pan = 90					  	  # location                             ############
tilt = 90					  	  # while using                         #############
#use this tweak to change the moters middle position ###### software     ############
                                                                          ##      ###
                                                                           #      ###
                                                                                  ###
                                                                                  ###
                                                                                  ###
Drift = False                                                                     ###
count = 0                                                                         ###
devmode = 0                                                                       ###
devmodee = False                                                                  ###
bw.speed = 0                                                                      ###
                                                                                  ###
                                                                               #########
                                                                                #######
                                                                                 #####
                                                                                  ###
#use this to tweak the servos resting location  #     servo                        #
fw.turn(90)                                     #     resting
pan_servo.write(90)                             #     location (for before and after use of software)
tilt_servo.write(90)                            #     tweak
#use this to tweak the servos resting location  #     here


try:
	while True:
		char = screen.getch() # grabs the keystroke
		
		if char == ord('`'):
			break


		elif char == ord('a'):
			wheel = wheel - 90
			fw.turn(wheel)
		elif char == ord('d'):
			wheel = wheel + 90
			fw.turn(wheel)
		elif char == ord('e'):
			fw.turn(90)
		elif char == ord('w'):
			if Drift == False:
                                if count == 0:
                                        speed = 0
                                count = count + 1
#
			speed = speed + 20
			bw.backward()
			bw.speed = speed
		#	count = 0
		elif char == ord('r'):
			bw.stop()
			speed = 0
		elif char == ord('t'):
			fw.turn(90)
			pan_servo.write(100)
			tilt_servo.write(90)
		elif char == curses.KEY_LEFT:
			pan = pan + 60
			pan_servo.write(pan)
		elif char == curses.KEY_UP:
			tilt = tilt - 20
			tilt_servo.write(tilt)
		elif char == curses.KEY_RIGHT:
			pan = pan - 60
			pan_servo.write(pan)
		elif char == curses.KEY_DOWN:
			tilt = tilt + 20
			tilt_servo.write(tilt)
		elif char == ord('/'):
			devmode = devmode + 1
			if devmode == 5:
				devmodee = True
				print("dev mode activated")
				bw.speed = 0                            #resets all outputs to even   {
				fw.turn(90)  # numbers inputs can be 0-180 while 90 is even
				pan_servo.write(90)
				tilt_servo.write(90)                    #    }

				sleep(5)
				os.system('clear')
				devmode = 1
			elif devmode == 1:
				print(speed)
		elif char == ord('s'):
	#		if Drift == False:
	#			if count == 0:
			speed = 0
	#			count = count + 1
	#		speed = speed + 20
			bw.forward()
			bw.speed = 30
			count = 0
finally:
	curses.endwin()
	bw.speed = 0                            #resets all outputs to even   {
	fw.turn(90)  # numbers inputs can be 0-180 while 90 is even
	pan_servo.write(100)
	tilt_servo.write(90)                    #    }

