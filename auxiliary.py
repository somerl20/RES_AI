import librosa
import numpy as np
from playsound import playsound as play
def playNp(audioArr,fs=16000):
    librosa.output.write_wav('/home/london/PycharmProjects/echo/archiv/tempfile.wav',
                             audioArr, fs)

    play('/home/london/PycharmProjects/echo/archiv/tempfile.wav')

def add_noise(u,sd=0.01):
    size=u.size
    noise=np.random.normal(0,sd,size)
    return np.add(u,noise)