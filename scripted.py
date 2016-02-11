#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17]


# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.LOW)

#function definitions

def flicker(beats_per_minute, flicker_time, *port_number):  
  starting_time = time.time()
  flickers_per_second = 1 / (float(beats_per_minute) / 60)
  print flickers_per_second
  while ((time.time() - starting_time) <= flicker_time): 
    for j in port_number:
      GPIO.output(j, GPIO.HIGH)
    time.sleep(flickers_per_second);
    for k in port_number:
      GPIO.output(k, GPIO.LOW)
    time.sleep(flickers_per_second);

def turn_on(on_length, *port_number):
  for j in port_number:
    GPIO.output(j, GPIO.HIGH)
  time.sleep(on_length)
  for j in port_number:
    GPIO.output(j, GPIO.LOW)

def whereami(start_time):
  print "Time:" + str(time.time() - start_time)
# main loop

try:
  start_time = time.time()
  #segment 1
  time.sleep(2.03) 
  whereami(start_time)
  turn_on(1.775, 2, 3 ,4, 17)
  time.sleep(0.125);
  turn_on(0.825, 2, 3 ,4, 17)
  time.sleep(0.138);
  turn_on(0.874, 2, 3 ,4, 17)
  time.sleep(0.113);
  turn_on(1.913, 2)
  turn_on(1.86, 3)
  turn_on(1.912, 4)
  turn_on(1, 17)
  #drum kick
  turn_on(0.212, 2, 3)
  turn_on(0.25, 4, 17)
  turn_on(0.25, 2, 3)
  turn_on(0.263, 4, 17)
  #verse
  #EEEE
  turn_on(0.212, 2, 3, 4, 17)
  time.sleep(0.251)
  #OW
  turn_on(0.262, 3, 4)
  turn_on(0.688, 2, 17)
  turn_on(0.225, 2)
  turn_on(0.237, 17)
  #DUN
  turn_on(0.238, 2, 4, 3, 17)
  time.sleep(.237)
  #Raise your backs
  turn_on(0.238, 4, 17)
  turn_on(0.112, 2, 3) 
  time.sleep(0.113)
  turn_on(0.475, 2, 3)
  #OHH
  turn_on(0.2, 2, 3, 4, 17)
  time.sleep(0.262)
  #In the rock
  turn_on(0.5, 2, 3, 4, 17)
  turn_on(0.238, 2)
  turn_on(0.237, 3)
  turn_on(0.475, 2, 3, 4, 17)
  turn_on(0.25, 2)
  turn_on(0.25, 3)
  turn_on(0.263, 2, 3, 4, 17)
  #around the world
  turn_on(0.4, 2)
  turn_on(0.5, 3)
  turn_on(0.312, 4)
  turn_on(0.20, 2,3,4,17)
  whereami(start_time)
  #20.9  
  turn_on(0.513,2, 3, 4, 17)#total time
  turn_on(0.262,2, 3, 4, 17)#total time
  turn_on(0.463,3,4)#total time
  turn_on(0.225,2,17)#total time
  turn_on(0.45,2)#total time
  turn_on(0.25,3,4,17)#total time
  turn_on(0.25,3,4,17)#total time
  turn_on(0.262,3,4,17)#total time
  whereami(start_time)
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
