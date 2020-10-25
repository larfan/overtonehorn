import time
import pygame
import pyaudio
import struct
import numpy as np
#just for devices
import sounddevice as sd
print(sd.query_devices())

CHUNKSIZE = 1024 # fixed chunk size
p = pyaudio.PyAudio()
fs=44100
filename='/home/larfan/Documents/PythonProgramming/overtone_horn/finalsoundsamples/2lamour.wav'
#open 
pygame.mixer.pre_init()
pygame.mixer.init()
#pygame.mixer.Sound.load(filename)
chunk = 1024*4  
class record:
    def __init__(self):
        self.stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True, frames_per_buffer=CHUNKSIZE,input_device_index=4)
        self.SHORT_NORMALIZE=(1.0/32768.0)
       
    def amplitude(self):
        #calculate RMS(quadratisches Mittel,https://de.wikipedia.org/wiki/Effektivwert)
            self.check=self.stream.read(int(0.01*fs),exception_on_overflow = False)        #measure small block
            count = len(self.check)/2
            format = "%dh"%(count)
            shorts = struct.unpack( format, self.check )
            # iterate over the block.
            sum_squares = 0.0
            for sample in shorts:
                # sample is a signed short in +/- 32768. 
                # normalize it to 1.0
                n = sample * self.SHORT_NORMALIZE
                sum_squares += n*n
            self.amp=np.sqrt( sum_squares / count )
            
            print(self.amp)
            if self.amp <=0.2:
                return False
            else:
                return True
    
rec=record()

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
        #    pygame.mixer.unpause()
    def testfuntion(self):
        print('hi')
        

out=output()
out.actualoutput()

timeend=time.time()-1
print(timeend)
while True:
    if rec.amplitude() == True:
        if statussound == False:
            timedifference=time.time()-timeend  #apparently not in secs
            print('Timediffernece: ', timedifference)
            if usedbefore == True and timedifference<1:         #timedifference<n in case of glitch in amplitude
                pygame.mixer.unpause()
                statussound=True
                print('do you enter?')
                
            else:
                out.actualoutput()
                print('Activating stream')
        timeend=time.time()     #last time mic's amplitude was high enough
    else:
        pygame.mixer.pause()
        statussound=False
    time.sleep(0.05)





