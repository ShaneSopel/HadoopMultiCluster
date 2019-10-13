#Intended use by Shane Sopel for Hadoop Edge Project ECE 578 Umich Dearborn 
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(7.5)

#Open File
text_file = open("servoData.txt", "w")

#Print the Program Title
print "Hadoop Servo Module 0.a"
print "This program is intended to run on python 2.7"
print "Starting Servo Module"
print "Running for Approximately 20 Cycles"

cycle = 0
#While cycle is less than 20..
while cycle < 20:
	#turn towards 90 degree
        p.ChangeDutyCycle(7.5)
	text_file.write("quarter \n")
        time.sleep(1)
	#turn towards 90 degree 
        p.ChangeDutyCycle(2.5)
	text_file.write("half \n")
        time.sleep(1)
	#turn towards 180 degree
        p.ChangeDutyCycle(12.5)
	text_file.write("full \n")
        time.sleep(1)
	cycle += 1
	print "cycle: {0}".format(cycle)
text_file.close() 
