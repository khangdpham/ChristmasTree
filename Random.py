from gpiozero import LED
from time import sleep
import random
import threading
import sys
import pygame
pygame.mixer.init()
pygame.mixer.music.load("SugarPlum.wav")
pygame.mixer.music.play()


bpm= 121
bps = 121*1.0/60/8

relays= [ LED(4),LED(17) ,LED(27),LED(22) ,
         LED(12),LED(16) ,LED(20),LED(21) ]
prev_x= 0
prev_y= 0
x = 0
def relayLed():
  threading.Timer(bps,relayLed).start()
  [l.off() for l in relays]
  
  x = random.randint(0,7)
  y = random.randint(0,7)
  while y == x and (x == prev_x or y == prev_y) :
    x = random.randint(0,7)
    y = random.randint(0,7)
  prev_x = x
  prev_y = y
  relays[x].on()
  relays[y].on()




relayLed()
while pygame.mixer.music.get_busy() == True:
    continue
sys.exit()
