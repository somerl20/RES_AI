import adaptfilt
import numpy as np
class AecFilter():
    def lms(self, y, x ):
        M = 10000
        lr = 0.01
        yEs, eEs,h = adaptfilt.lms(u=y, d=x, M=M, step=lr)
        y_con=np.convolve(x,h,'same')
        e_conv=y-y_con
        return y_con,e_conv
    def nlmsru(u, d, M, step, eps=0.001, leak=0, initCoeffs=None,
               N=None, returnCoeffs=False):
        y,e,w=adaptfilt.nlmsru(u, d, M, step, eps=0.001, leak=0,initCoeffs=None, N=None, returnCoeffs=False)
        return e#,y
