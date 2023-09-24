# import pandas as pd #load and process data 
import numpy as np # numercal methods
#import numdifftools as nd
import matplotlib.pyplot as plt #plotting 
# import matplotlib.ticker as ticker #plotting misc
import scipy.optimize as opt
# from scipy.optimize import LinearConstraint
import plotly.graph_objects as go
import plotly.io as io 

io.renderers.default ="browser"
def f_funct(var):
    x= var[0]
    y= var[1]
    return (3*x**2)+2*x*y+(4*y**2)-6*x-8*y+5

def g_funct(var):
    x= var[0]
    y= var[1]
    return (x**2+3*y**2)**2-2*x*y



x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)

X, Y = np.meshgrid(x,y)
initial_guess = [0, 0]
Z = (X**2+3*Y**2)**2-2*X*Y
#Z= 3*X**2+2*X*Y+4*Y**2-6*X-8*Y+5
fig = go.Figure(data=[go.Surface(z=Z,x=X, y=Y)])

fig.show()

result = opt.minimize(f_funct,initial_guess,method='BFGS' )
print(result.message)
print("Minimum value: ",result.fun)
print(" Minimum coordianates: ", result.x)
# x = np.linspace(-5,5,1000)
# y = np.linspace(-5,5,1000)

# X, Y = np.meshgrid(x,y)
# initial_guess = [0, 0]


# result = opt.minimize(f_funct,initial_guess,method='BFGS' )
# print(result.message)
# print("Minimum value: ",result.fun)
# print(" Minimum coordianates: ", result.x)