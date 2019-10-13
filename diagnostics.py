#Intended use by Shane Sopel & Anthony Torres for Hadoop Edge Project ECE 578 Umich Dearborn 

import RPi.GPIO as GPIO
import time
from colorama import Fore


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31 ,GPIO.OUT)

#Print the Program Title
print "Hadoop diagnostics Module 0.a"
print "This program is intended to run on python 2.7"

#Open File for Servo Data
text_file1 = open("HadoopServoData/part-r-00000", "r")
lineservo = text_file1.readline() 

#Open File for LED Data
text_file = open("HadoopLEDData/part-r-00000", "r")
lineled = text_file.readline() 

cycle = 0
#While cycle is less than 5..
while cycle < 5:
	#If the Servo value is equal to full 20
        if lineservo.strip() == "full	20":
	        print Fore.GREEN+"Servo is operating at correctly"
		time.sleep(.5)

	#If the LED value is equal to blue  20
	if lineled.strip() == "BLUE	20":
		#set buzzer pin high
		GPIO.output(31, GPIO.HIGH)
		print Fore.RED+"ALERT"
		print "Blue Warning LED Initiated 20 times"
		print "Engine Failer"
		time.sleep(.5)
		#set buzzer pin low
		GPIO.output(31, GPIO.LOW)
	cycle += 1
text_file.close()
text_file1.close()
