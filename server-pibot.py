#Imports modules
import socket
import RPi.GPIO as GPIO
import time
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
import os


picar.setup()
os.system('clear')							
bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)
picar.setup()




wheel = 90					   	
speed = 0					  	 
pan = 90					  	  
tilt = 90	

cmd = False

fw.turn(90)                                   
pan_servo.write(90)                            
tilt_servo.write(90)


listensocket = socket.socket() #Creates an instance of socket
Port = 8080 #Port to host server on
maxConnections = 999
IP = socket.gethostname() #IPess of local machine

listensocket.bind(('',8000))

#Starts server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True

#Sets up the GPIOs --Can only be used on Raspberry Pi
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

while running:
    message = clientsocket.recv(1024).decode() #Gets the incomming message
    print(message)
    if cmd == True:
        os.system(message)
        cmd = False
    elif message == "left":
        fw.turn(0)
    elif message == "right":
        fw.turn(180)
    elif message == "forward":
        bw.backward()
        bw.speed = 50
    elif message == "stop":
        bw.stop()
    elif message == "straight":
        fw.turn(90)
    elif message == "backwards":
        bw.forward()
        bw.speed = 50
    elif message == "cmd":
        cmd = True
    if not message == "":
        GPIO.output(7,True)
        time.sleep(5)
        GPIO.output(7,False)
