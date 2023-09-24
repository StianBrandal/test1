import pandas as pd #load and process data 
import numpy as np # numercal methods
import matplotlib.pyplot as plt #plotting 
import matplotlib.ticker as ticker #plotting misc
import scipy.optimize as opt
from scipy.optimize import LinearConstraint

#read csv-file. Note thate comma (,) is used as decimal symbol (nordic standard), thus semicolon is used as seperator
data= pd.read_csv("C:/Users/stian/OneDrive/Documents/Skule/ADA501/Øvinger/Øving 2/svalbard_met.csv", sep =';')

# Select data column containing average mounthly temperature. 
# The data is loaded as a string in order to handle the comma
temperature =np.array(data['Homogenisert middeltemperatur (mnd)'].values.astype(str))

#replacing comma with dot (as decimal symbol)
temperature = np.char.replace(temperature,',','.')
temperature = temperature.astype(float)

#reading timepoints. String on the format mm.yyyy
timepoints =np.array(data['Tid(norsk normaltid)'].values.astype(str))


temperature = temperature[0:12*20]
timepoints = timepoints[0:12*20]

t = np.array(range(timepoints.shape[0]))

def f_sin(t,a):
    return a[0]*np.sin(a[1]*t+a[2])+a[3]


def C(a):
    return np.linalg.norm(f_sin(t,a)-temperature)



inistal_gues = np.array([12.19941282,  0.52876367,  2.19580259, -7.82113779])

#constr = LinearConstraint([0,1,0,0],[0.3], [1])

result = opt.minimize(C,inistal_gues)

print(result.x)
print(result.fun)
plt.plot(t,temperature,"o")
plt.plot(t,f_sin(t,result.x))
plt.show()



# #construct figure with landscape format
# plt.figure(figsize=(12, 3))
# #establsih subplot (we only nee one plot, but will need the attributes in the subplot routine)
# temp_plot = plt.subplot()

# #plot the time series
# plt.plot(timepoints ,temperature)
# #changing the marks on the x-axis
# temp_plot.xaxis.set_major_locator(ticker.IndexLocator(base=120, offset=5))
# #rotate the text on the x-axis, making it easier to read
# temp_plot.tick_params(labelrotation=70)

# plt.show()



