#!/usr/bin/python3

import pandas as pd # we're converting CSV into DataFrame for easier access of data

iris= pd.read_csv("iris.csv") #importing CSV file into DataFrame


sl=iris["sepal.length"] #calling data by column and directly appyling math as follows 
slmean=sl.mean()
slmedian=sl.median()
slmode=sl.mode()[0]

sw=iris["sepal.width"]
swmean=sw.mean()
swmedian=sw.median()
swmode=sw.mode()[0]

pl=iris["petal.length"]
plmean=pl.mean()
plmedian=pl.median()
plmode=pl.mode()[0]

pw=iris["petal.width"]
pwmean=pw.mean()
pwmedian=pw.median()
pwmode=pw.mode()[0]

import matplotlib.pyplot as plt # for making plot
import numpy as np 

#plot 1, we're creating sublpot 
x=np.array(["slmean", "swmean", "plmean", "pwmean"])
y=np.array([slmean, swmean, plmean, pwmean])

plt.subplot(1,3,1) # arguments 1 row, 3 column, and it's first graph
plt.barh(x,y, height= 0.6, color= "red")
plt.title("comparative Mean")

#plot 2
x=np.array([ "slmedian", "swmedian", "plmedian", "pwmedian"])
y=np.array([ slmedian, swmedian, plmedian, pwmedian])
plt.subplot(1,3,2)
plt.barh(x,y, height= 0.6, color= "blue")
plt.title("comparative Median")


#plot 3
x=np.array(["slmode", "swmode", "plmode", "pwmode"])
y=np.array([slmode, swmode, plmode, pwmode])
plt.subplot(1,3,3)
plt.barh(x,y, height= 0.6, color= "green")
plt.title("comparative Mode")

plt.suptitle("Comparative test study")
plt.show()