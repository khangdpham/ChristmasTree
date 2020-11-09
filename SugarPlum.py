from gpiozero import LED
from time import sleep
import random
import threading
import sys, mido
import pygame
pygame.mixer.init()
pygame.mixer.music.load("SugarPlum.wav")
pygame.mixer.music.play()


bpm= 121
bps = 121*1.0/60/4

relays= [ LED(4),LED(17) ,LED(27),LED(22) ,
         LED(12),LED(16) ,LED(20),LED(21) ]

pitch = 0
pygame.mixer.init()
pygame.mixer.music.load("SugarPlum.wav")
m = mido.MidiFile('SugarPlum.mid')

def myround(x, base=5):
    return base * round(x/base)



pygame.mixer.music.play()

for x in m.play():
  if len(x.bytes()) != 3:
    continue
  pitch = myround(x.bytes()[2],base=5)
  vel = myround(x.bytes()[1],base=5)
  print(x)
  
  #print(x) 
  if x.type == "note_off":
    relays[int(pitch/8)%7].off()
  if x.type == "note_on":
    relays[int(vel/8)%7].on()
 
