#!/usr/bin/python
import RPi.GPIO as GPIO
import curses
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17]
keys_to_lights = {
  '81': [2],
  '87': [3],
  '69': [4],
  '82': [17],
  '65': [2, 3],
  '83': [4, 17],
  '68': [2, 4],
  '70': [3, 17],
  '90': [2, 17],
  '88': [3, 4],
  '67': [2, 3, 4],
  '86': [3, 4, 17],
  '32': [2, 3, 4, 17]
};


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

def turn_on(port_number):
  for j in port_number:
    GPIO.output(j, GPIO.HIGH)
  return True

def turn_off():
  for j in pinList:
    GPIO.output(j, GPIO.LOW)
  return False

def whereami(start_time):
  print "Time:" + str(time.time() - start_time)

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    xyz = False
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            turn_off()
            stdscr.addstr(str(c) + 'HI')
            for key, value in keys_to_lights.iteritems():
              if (c == ord(chr(int(key)).lower())):
                stdscr.addstr(str(value) + ' GGG')
                turn_on(value)
             
           
        # print numeric value
        stdscr.refresh()
        # return curser to start position
        stdscr.move(0, 0)

try:
  curses.wrapper(main)

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
