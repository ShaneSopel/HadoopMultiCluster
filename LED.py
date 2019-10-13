#Intended use by Shane Sopel & Anthony Torres for Hadoop Edge Project ECE 578 Umich Dearborn 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(37 ,GPIO.OUT)
GPIO.setup(35 ,GPIO.OUT)
GPIO.setup(33 ,GPIO.OUT)

#Open File
text_file = open("LEDdata.txt", "w")

#Print the Program Title
print "Hadoop LED Module 0.a"
print "This program is intended to run on python 2.7"
print "Starting LED Module"
print "Running for Approximately 20 cycles"

cycle = 0
while cycle < 20:
	#light RGB Red
	GPIO.output(37, GPIO.HIGH)
	time.sleep(.5)
	GPIO.output(37, GPIO.LOW)
	time.sleep(.5)
	text_file.write("RED \n")
	#light RGB Green
	GPIO.output(35, GPIO.HIGH)
	time.sleep(.5)
	GPIO.output(35, GPIO.LOW)
	time.sleep(.5)
	text_file.write("GREEN \n")
	#light RGB Blue
	GPIO.output(33, GPIO.HIGH)
	time.sleep(.5)
	GPIO.output(33, GPIO.LOW)
	time.sleep(.5)
	text_file.write("BLUE \n")
	cycle += 1
        print "cycle: {0}".format(cycle)
text_file.close()

