import time
import pygame
import pyaudio
import struct
import numpy as np
#just for devices
import sounddevice as sd
import os
print(sd.query_devices())

CHUNKSIZE = 1024 # fixed chunk size
p = pyaudio.PyAudio()
fs=44100
scriptdir=script_dir = os.path.dirname(__file__)
realpath='finalsoundsamples/hornsound.wav'
absfilepath=os.path.join(script_dir,realpath)
filename=absfilepath
#open 
pygame.mixer.pre_init()
pygame.mixer.init()
#pygame.mixer.Sound.load(filename)
chunk = 1024*4  


statussound=False
usedbefore=False
class output:
    def __init__(self):
        pass
    def actualoutput(self):
        global statussound
        statussound=True        #indator if its currently playing sound
        global usedbefore
        usedbefore=True
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(filename),-1)       #to repeat file
        time.sleep(100)
        #    pygame.mixer.unpause()
    def testfuntion(self):
        print('hi')
        

out=output()
out.actualoutput()








