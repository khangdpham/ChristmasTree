from gpiozero import LED
from time import sleep
import random
import threading
import sys, mido
import pygame


song_name="Wizards"
pygame.mixer.init()
pygame.mixer.music.load(song_name+".wav")
pygame.mixer.music.play()

bpm= 142
bps = 121*1.0/60/4

relays= [ LED(4),LED(17) ,LED(27),LED(22) ,
         LED(12),LED(16) ,LED(20),LED(21) ]

pitch = 0
pygame.mixer.init()
pygame.mixer.music.load(song_name+".wav")
m = mido.MidiFile('SugarPlum.mid')

def myround(x, base=5):
    return base * round(x/base)

pygame.mixer.music.play()
for x in m.play():
  pitch = myround(x.bytes()[1],base=5)
  if len(x.bytes()) != 3:
    continue
  
  if x.type == "note_off":
    relays[int(pitch/5)%7].off()
  #print(int(pitch/10)%7)
  if x.type == "note_on":
    relays[int(pitch/5)%7].on()
 
