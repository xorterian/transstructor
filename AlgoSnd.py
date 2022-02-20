# Run Cmd as admin, e.g.: C:\Python386\python.exe AlgoSnd.py "((-t&4095)*(255&t*(t&t>>13))>>12)+(127&t*(234&t>>8&t>>3)>>(3&t>>14))" 500000 result.wav
from LogFun import *
import numpy as np
import cv2
import math
from scipy.io.wavfile import write
import wave
import optparse

parser = optparse.OptionParser(usage = 'usage: %prog [function of t] [length (ms)] [output filename]')
options, args = parser.parse_args()
#print("options: ",options)
print("args: ",args)
F = args[0]
L = int(args[1])
fname = args[2]
fs = 44100
if F=='':
   F=ranlogfun()
   print('Let F be:',F)

def readM(name):
    music = wave.open(name)
    samples = music.getnframes()
    audio = music.readframes(samples)
    audio = np.frombuffer(audio, dtype=np.int16).astype(np.float32) / 2 ** 15
    return audio

def speeder(u,rate):
    return [ u[math.floor(t*rate)%len(u)] for t in range(math.floor(len(u)/rate)) ]

codingRate = 2**12-1

exec('snd = np.array([ '+F+'%4096 for t in range(L) ])',globals())
snd = snd / np.max(np.abs(snd))
write(fname,fs*2,(snd*2**15).astype(np.int16))
