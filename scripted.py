# This is how you (#include) stuff in python
import RPi.GPIO as GPIO
import time

# This does somthing important
GPIO.setmode(GPIO.BCM)

# This is how you delclare variables in Python. No need for prefixes like int, void, string, char, etc
# Sets a variable named pin_list equal to array
pin_list = [1,2,3,4,5,6,7,8]

pin_list_name = { "front_top_right":1,
"front_top_left":1, 
"front_bottom_left":1, 
"front_bottom_right":1,
"back_top_right":1,
"back_top_left":1, 
"back_bottom_left":1, 
"back_bottom_right":1 }

# This is a range based for loop. In other words, the variable (i) will be set to (2), runs through the code, 
# (3) then runs through the code, (4) then etc, then(17)
for i in pin_list: # First run: i = 2
    # This initializes i to GPIO.OUT. In other words, this allows us to turn off an on lights.
    GPIO.setup(i, GPIO.OUT) 

    # GPIO.output accepts 2 parameters.
    # Parameter 1: light you want to manipulate
    # Parameter 2: turns light on or off.
      # GPIO.LOW = off
      # GPIO.HIGH = on 
    GPIO.output(i, GPIO.LOW)  

#function definitions
# Parameter 1: a number specifying how long you want to turn the light on for
# Parameter 2: an array of what lights you want to turn on
def turn_on(on_length, port_number):
  for j in port_number:
    GPIO.output(j, GPIO.HIGH)
  time.sleep(on_length)
  for j in port_number:
    GPIO.output(j, GPIO.LOW)

def whereami(start_time):
  print "Time:" + str(time.time() - start_time)
# main loop

try:
  turn_on(5, ["front_bottom_right", "front_bottom_left"] )

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


