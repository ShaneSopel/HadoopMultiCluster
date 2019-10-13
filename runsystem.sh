#!/bin/bash

echo "Hadoop Edge Server Implementation 0.a"
echo "Running the LED and Servo Modules"
 
echo "LED Module" 
python LED.py

echo "Servo Module"
python servo.py

echo "Hadoop Servo Processing"
hadoop fs -put ~/servoData.txt /input_dir
hadoop jar ~/WordCount.jar WordCount /input_dir /output_dir1
hadoop fs -get /output_dir1 ~/HadoopServoData

echo "Hadoop LED Processing"
hadoop fs -put ~/LEDdata.txt /input_dir
hadoop jar ~/WordCount.jar WordCount /input_dir /output_dir 
hadoop fs -get /output_dir ~/HadoopLEDData

echo "LED Processing Encounter Error"
python buzzer.py


