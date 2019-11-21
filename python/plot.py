import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from splineclass import spline as sp

if __name__ == "__main__":

    print("Please enter a file name. ('.csv' is not required)")
    filename = input()
    
    df = pd.read_csv('../csv/'+filename+'.csv')

    xorigin, yorigin = (df['x'], df['y'])

    xa, ya = sp.splineInterpld(df, 100)
    xb, yb = sp.splineAkima1DInterpolator(df, 100)
    xc, yc = sp.splineSplprep(df, 100, 3)

    plt.figure(figsize=(12, 2)) 

    plt.subplot(1,4,1)
    plt.plot(xorigin, -yorigin, linestyle="none", marker="o")
    plt.title("origin")

    plt.subplot(1,4,2)
    plt.plot(xa, -ya)
    plt.title("interpld")

    plt.subplot(1,4,3)
    plt.plot(xb, -yb)
    plt.title("Akima1DInterpolator")

    plt.subplot(1,4,4)
    plt.plot(xc, -yc)
    plt.title("Splprep")

    plt.savefig('../image/'+filename+'.png')

    #This time series data is only increasing along the x-axis.
    # df1 = pd.read_csv('../csv/increasing.csv')

    # xorigin1, yorigin1 = (df1['x'], df1['y'])

    # x1, y1 = sp.splineInterpld(df1, 100)
    # x2, y2 = sp.splineAkima1DInterpolator(df1, 100)
    # x3, y3 = sp.splineSplprep(df1, 100, 3)

    # plt.figure(figsize=(12, 2)) 

    # plt.subplot(1,4,1)
    # plt.plot(xorigin1, -yorigin1, linestyle="none", marker="o")
    # plt.title("origin")

    # plt.subplot(1,4,2)
    # plt.plot(x1, -y1)
    # plt.title("interpld")

    # plt.subplot(1,4,3)
    # plt.plot(x2, -y2)
    # plt.title("Akima1DInterpolator")

    # plt.subplot(1,4,4)
    # plt.plot(x3, -y3)
    # plt.title("Splprep")

    # plt.savefig('../image/increasing.png')


    #This time series data includes a decreasing trend with respect to the x-axis.
    # df2 = pd.read_csv('../csv/complex.csv')

    # xorigin2, yorigin2 = (df2['x'], df2['y'])

    # x4, y4 = sp.splineInterpld(df2, 100)
    # x5, y5 = sp.splineAkima1DInterpolator(df2, 100)
    # x6, y6 = sp.splineSplprep(df2, 100, 3)

    # plt.figure(figsize=(12, 2)) 

    # plt.subplot(1,4,1)
    # plt.plot(xorigin2, -yorigin2, linestyle="none", marker="o")
    # plt.title("origin")

    # plt.subplot(1,4,2)
    # plt.plot(x4, -y4)
    # plt.title("interpld")

    # plt.subplot(1,4,3)
    # plt.plot(x5, -y5)
    # plt.title("Akima1DInterpolator")

    # plt.subplot(1,4,4)
    # plt.plot(x6, -y6)
    # plt.title("Splprep")

    # plt.savefig('../image/complex.png')
