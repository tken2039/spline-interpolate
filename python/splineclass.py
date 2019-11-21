import numpy as np
from scipy import interpolate
import pandas as pd

class spline:

    def __init__(self):
        self.name = ""

    #interpld
    def splineInterpld(xydata,point):
        try:
            x, y = spline.transnp(xydata)
            f = interpolate.interp1d(x, y,kind="cubic") #kindの値は一次ならslinear、二次ならquadraticといった感じに
            X = np.linspace(x[0],x[-1],num=point,endpoint=True)
            Y = f(X)
            return X,Y
        except ValueError as e:
            print("catch ValueError", e)
            return (0,0)

    #Akima1DInterpolator
    def splineAkima1DInterpolator(xydata,point):
        try:
            x, y = spline.transnp(xydata)
            f = interpolate.Akima1DInterpolator(x, y)
            X = np.linspace(x[0],x[-1],num=point,endpoint=True)
            Y = f(X)
            return X,Y
        except ValueError as e:
            print("catch ValueError", e)
            return (0,0)

    #splprep
    def splineSplprep(xydata,point,deg):
        x, y = spline.transnp(xydata)
        tck,u = interpolate.splprep([x,y],k=deg,s=0) 
        u = np.linspace(0,1,num=point,endpoint=True) 
        XY = interpolate.splev(u,tck)
        return XY[0],XY[1]
    
    #pd to np
    def transnp(array):
        if type(array) == pd.DataFrame:
            array = np.array(array.T)
            npa1, npa2 = (array[0], array[1])
            return npa1, npa2
        elif type(array) == np.ndarray:
            npa1, npa2 = (array.T[0], array.T[1])
            return npa1, npa2
        else:
            print("Take pd.DataFrame or np.ndarray!")
