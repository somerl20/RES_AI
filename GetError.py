from sklearn.metrics import mean_squared_error as immse
from sklearn.metrics import mean_absolute_error as iabs
class GetError():

    def mse(self,s,sd):
        erMse= immse(s,sd)
        erAbs=iabs(s,sd)
        print 'erMse:' +str(erMse)+ ' erAbs: '+str(erAbs)
        #return erMse,erAbs
