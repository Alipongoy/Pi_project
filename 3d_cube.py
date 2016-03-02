# This is how you (#include) stuff in python
import RPi.GPIO as GPIO
import time

# This does somthing important
GPIO.setmode(GPIO.BCM)

# This is how you delclare variables in Python. No need for prefixes like int, void, string, char, etc
# Sets a variable named pinList equal to array
pinList = [2, 3, 4, 17]


# This is a range based for loop. In other words, the variable (i) will be set to (2), runs through the code, 
# (3) then runs through the code, (4) then etc, then(17)
for i in pinList: # First run: i = 2
    # This initializes i to GPIO.OUT. In other words, this allows us to turn off an on lights.
    GPIO.setup(i, GPIO.OUT) 

    # GPIO.output accepts 2 parameters.
    # Parameter 1: light you want to manipulate
    # Parameter 2: turns light on or off.
      # GPIO.LOW = off
      # GPIO.HIGH = on 
    GPIO.output(i, GPIO.LOW)  

#function definitions

# This is a test function. Don't mind this
# def flicker(beats_per_minute, flicker_time, *port_number):  
#   starting_time = time.time()
#   flickers_per_second = 1 / (float(beats_per_minute) / 60)
#   print flickers_per_second
#   while ((time.time() - starting_time) <= flicker_time): 
#     for j in port_number:
#       GPIO.output(j, GPIO.HIGH)
#     time.sleep(flickers_per_second);
#     for k in port_number:
#       GPIO.output(k, GPIO.LOW)
#     time.sleep(flickers_per_second);


# This is a function that I made which turns on and off lights for a specific amount of time
# Parameter 1: this a number which determines how long you are turning on an LED for.
# Parameter 2: this is an array of which lights you want to turn on. 
  # For example, passing [2,3,4] would turn on LEDS at 2,3,4 for on_length
def turn_on(on_length, *port_number): 
  # Range based for loop 
  for i in port_number:
    # turns i (LED port) on
    GPIO.output(i, GPIO.HIGH)
  # Sleeps for on_length. The reason for this is becuase if you turn on and off a light, there is no delay, which means
  # The light would not even turn on.
  time.sleep(on_length)
  # turns i (LED port) off
  for i in port_number:
    GPIO.output(i, GPIO.LOW)

def whereami(start_time):
  print "Time:" + str(time.time() - start_time)

# This is the int main() of the program.
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


