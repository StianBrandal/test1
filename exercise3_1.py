import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as io 
import scipy.optimize as opt

#io.renderers.default ="browser"

def funct_f(var):
    x= var[0]
    y= var[1]
    return x**2+(y**2)-4*x+6*y+9


def funct_g(var):
    x= var[0]
    y= var[1]

    return ((x+2*y-7)**2)+ (2*x+y-5)**2


def funct_h(var):
    x= var[0]
    y= var[1]
    return (x**2+y-11)**2+(x+y**2-7)**2

x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)

X, Y = np.meshgrid(x,y)
initial_guess = [0, 0]


result = opt.minimize(funct_f,initial_guess,method='BFGS' )
print(result.message)
print("Minimum value: ",result.fun)
print(" Minimum coordianates: ", result.x)
#Z = X**2+(Y**2)-4*X+6*Y+9   # convex and bounded below  because its second degree polynom 
#Z = ((X+2*Y-7)**2)+ (2*X+Y-5)**2 # convex and bounded below  because its second degree polynom 
#Z = (X**2+Y-11)**2+(X+Y**2-7)**2  # not convex and not bounded because its fourth degree polynom 
fig = go.Figure(data=[go.Surface(z=Z,x=X, y=Y)])

#fig.show()



# xlist_f = np.linspace(-20,20,num=10000)  # np.arrange(-10,10,.01)
# ylist_f=funct_g(xlist_f,1)


# xlist_g = np.linspace(-1000,1000,num=1000)
# ylist_g = funct_g(xlist_f,5)
# xlist_h = np.linspace(-10,10,num=1000)
# ylist_h = funct_h(xlist_f,5)  

# plt.figure(num=0,dpi=120)
# plt.plot(xlist_f,ylist_f,label="F function")    #bounded below vil aldri gå under det punktet, yes function is convex
# plt.plot(xlist_g,ylist_g,label="G function")   #bounded below vil aldri gå under det punktet , yes function is convex
# plt.plot(xlist_h,ylist_h,label="H function")   #bounded below vil aldri gå under det punktet , yes function is convex
# plt.grid(True)
# plt.legend() 
# plt.show()


# initial_guess = [0, 0]


# result = opt.minimize(funct_f,initial_guess,method='BFGS' )
# print(result.message)
# print("Minimum value: ",result.fun)
# print(" Minimum coordianates: ", result.x)