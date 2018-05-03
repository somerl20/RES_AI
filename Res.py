import numpy as np
from ResFilter import ResFilter
from GetError import GetError
class Res():
    def __init__(self):
        self.L=640
        self.funcdict={'IRM':ResFilter.IRM,'IAM':ResFilter.IAM,'PSF':ResFilter.PSF}
        self.sd=np.array()
    def res(self,e,s,x=None,y=None,name='PSF'):
        if e.size!=s.size:
            print "s and e are not equal"
            return
        for i in range(0,(e.size)/self.L):
            eSegment=e[i*(self.L):(i+1)*self.L]
            sSegment=s[i*(self.L):(i+1)*self.L]
            sd=self.funcdict[name](e,s,x=None,y=None)
            self.sd=np.hstack((self.sd,sd))
        GetError.mse(s,sd)
        return sd







