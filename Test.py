from gpiozero import LED
from time import sleep
import random
import threading
import sys, mido
import pygame
from timeit import default_timer
bpm= 121
bps = 121*1.0/60/4

relays= [ LED(4),LED(17) ,LED(27),LED(22) ,
         LED(12),LED(16) ,LED(20),LED(21) ]

'''
for x in range(8):
 relays[x].on()
 sleep(.5)
sys.exit(1)
'''

song_name = "Wizards"
song_name = "SugarPlum"
pygame.mixer.init()
pygame.mixer.music.load(song_name+".wav")
def RelayOff():
  threading.Timer(off_dur,RelayOff).start() 
  [ x.off() for x in relays ]


ff=open(song_name+".bt","r")

m = mido.MidiFile(song_name+".mid")
off_dur= .25/2

ln = ff.readline()
pygame.mixer.music.play()

start = default_timer()

def ProcessInput(s):
  if 'x' in s: # hex
    return bin(int(str(s),16))[2:].zfill(8)
  elif 'b' in s: # binary
    return str(s)[2:].zfill(8)
  return bin(int(str(s)))[2:].zfill(8)
 
def RelaysCtl(mask):
  for x in range(len(mask)):
    if mask[x] == "1":
      relays[x].on()
    else:
      relays[x].off()


while ln:
  mark = round(default_timer()-start,2)
  if mark > float(ln.split(',')[0]):
    r = ln.split(',')[1]
    print(mark," :",ln,"=>",r)
    RelaysCtl(ProcessInput(r))
    ln = ff.readline()



