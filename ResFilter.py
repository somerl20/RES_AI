import numpy as np
from numpy import hanning
from numpy.fft import  ifft
from numpy import fft, angle
from math import sqrt, cos

class ResFilter():
    def __init__(self):
        self.N=1024
        self.window=hanning(self.N)
    def IRM(self,e,s,x=None,y=None):
        z=e-s
        e=np.multiply(e,self.window)
        s=np.multiply(s,self.window)
        z=np.multiply(z, self.window)
        Sf=fft(s,self.N)
        Zf=fft(z,self.N)
        Ef=fft(e,self.N)
        S=abs(Sf)
        Z=abs(Zf)
        numarator=S**2
        denominator=sqrt(s**2+Z*2)
        M=np.divide(numarator,denominator)
        sd=ifft(np.multiply(Ef,M))
        return sd

    def IAM(self,e,s,x=None,y=None):
        Sf = fft(s, self.N)
        Ef = fft(e, self.N)
        S = abs(Sf)
        E=abs(Ef)
        M = np.divide(S, E)
        sd = ifft(np.multiply(Ef, M))
        return sd
    def PSF(self,e,s,x=None,y=None):
        Sf = fft(s, self.N)
        Ef = fft(e, self.N)
        S = abs(Sf)
        E = abs(Ef)
        Sphase=angle(Sf)
        Ephase=angle(Ef)
        m1=np.divide(S, E)
        m2=cos(Sphase-Ephase)
        M = np.multiply(m1, m2)
        sd = ifft(np.multiply(Ef, M))
        return sd