import os
import wave
import numpy as np
from scipy.io.wavfile import read
import librosa
class AudioStorage():
    def __init__(self):
        self.path='/home/london/PycharmProjects/echo/audio'
        self.counter=0
        self.file=os.listdir(self.path)
        self.storage={}
        for fiename in self.file:
            x, sr = librosa.load(self.path + '/' + fiename + '/x.wav',sr=16000)
            y, sr = librosa.load(self.path + '/' + fiename + '/y.wav',sr=16000)
            s, sr = librosa.load(self.path + '/' + fiename + '/s.wav',sr=16000)
            self.append(x,y,s,fiename)
    def append(self,x,y,s,name):
        self.storage[name]=[x,y,s]

