from inputs import get_gamepad
import math
import threading
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
import picar
import os
import curses
sportmode = False
picar.setup()
os.system('clear')
bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)
picar.setup()
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
wheel = 90
speed = 0
pan = 90
tilt = 90
bw.speed = 0
right = 0
fw.turn(90)
pan_servo.write(90)
tilt_servo.write(90)
try:

	class XboxController(object):
	    MAX_TRIG_VAL = math.pow(2, 8)
	    MAX_JOY_VAL = math.pow(2, 15)
	    def __init__(self):
	        self.LeftJoystickY = 0
	        self.LeftJoystickX = 0
	        self.RightJoystickY = 0
	        self.RightJoystickX = 0
	        self.LeftTrigger = 0
	        self.RightTrigger = 0
	        self.LeftBumper = 0
	        self.RightBumper = 0
	        self.A = 0
	        self.X = 0
	        self.Y = 0
	        self.B = 0
	        self.LeftThumb = 0
	        self.RightThumb = 0
	        self.Back = 0
	        self.Start = 0
	        self.LeftDPad = 0
	        self.RightDPad = 0
	        self.UpDPad = 0
	        self.DownDPad = 0
	        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
	        self._monitor_thread.daemon = True
	        self._monitor_thread.start()
	    def read(self):
	        x = self.LeftJoystickX
	        y = self.LeftJoystickY
	        a = self.A
	        lt = self.LeftTrigger
	        rt = self.RightTrigger
	        b = self.X 
	        rb = self.RightBumper
	        if self.A == 1:#############  controls
	            print("a")
	            bw.backward()
			if sport:
				bw.speed = 100
			elif sport == False:
	            		bw.speed = 40
	        elif self.RightThumb == 1:
                        fw.turn(180)
	        elif self.LeftThumb == 1:
	            fw.turn(0)
	        elif self.A == 1:
	            bw.speed = 40
	        elif self.X == 1:
	            bw.forward()
	            bw.speed = 30
	        elif self.B == 1:
	            bw.stop()################ controls
	    def _monitor_controller(self):
	        while True:
	            events = get_gamepad()
	            for event in events:
	                if event.code == 'ABS_Y':
	                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL 
	                elif event.code == 'ABS_X':
	                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL 
	                elif event.code == 'ABS_RY':
	                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL 
	                elif event.code == 'ABS_RX':
	                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL 
	                elif event.code == 'ABS_Z':
	                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL 
	                elif event.code == 'ABS_RZ':
	                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL 
	                elif event.code == 'BTN_TL':
	                    self.LeftBumper = event.state
	                elif event.code == 'BTN_TR':
	                    self.RightBumper = event.state
	                elif event.code == 'BTN_SOUTH':
	                    self.A = event.state
	                elif event.code == 'BTN_NORTH':
	                    self.X = event.state
	                elif event.code == 'BTN_WEST':
	                    self.Y = event.state
	                elif event.code == 'BTN_EAST':
	                    self.B = event.state
	                elif event.code == 'BTN_THUMBL':
	                    self.LeftThumb = event.state
	                elif event.code == 'BTN_THUMBR':
	                    self.RightThumb = event.state
	                elif event.code == 'BTN_SELECT':
	                    self.Back = event.state
	                elif event.code == 'BTN_START':
	                    self.Start = event.state
	                elif event.code == 'BTN_TRIGGER_HAPPY1':
	                    self.LeftDPad = event.state
	                elif event.code == 'BTN_TRIGGER_HAPPY2':
	                    self.RightDPad = event.state
	                elif event.code == 'BTN_TRIGGER_HAPPY3':
	                    self.UpDPad = event.state
	                elif event.code == 'BTN_TRIGGER_HAPPY4':
	                    self.DownDPad = event.state				
	if __name__ == '__main__':
	    joy = XboxController()
	    while True:
	        print(joy.read())
finally:	
	curses.endwin()
	bw.speed = 0
	fw.turn(90)
	pan_servo.write(100)
	tilt_servo.write(90)
#thankyou for using my code, this code was heavily based and inspired on many projects, as in, the xbox controller software (https://stackoverflow.com/a/66867816) and the moter and servo controls are from sunfounders code for the ball track software.
