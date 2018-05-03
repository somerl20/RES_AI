from Res import Res
from AudioStorage import AudioStorage
import numpy as np
from auxiliary import playNp, add_noise
from GetError import GetError
from AecFilter import AecFilter

audio=AudioStorage()
Aec=AecFilter()
err=GetError()

l=audio.storage["steav_jim"]
x=l[0]
y=l[1]
err.mse(x,y)
yn=add_noise(y)
err.mse(yn,x)
e,yw=Aec.lms(yn,x)
err.mse(yw,y)