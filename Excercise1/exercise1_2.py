import numpy as np
import matplotlib.pyplot as plt

# Define function to be integrated
def f(x):
    f = x
    return f

# Define integral boundaries
a = 0
b = 1

intexact = np.exp(1)-np.exp(0)


def Trapezoidal(h,N,xpoints):
# Calculate sum using trapezoidal rule
    integral = 0
    for i in range(0,N):
        integral = integral + (f(xpoints[i])+f(xpoints[i+1]))/2*h
    return integral

def Midpoint(h,N,xpoints):
# Calculate sum using midpoint rule
    integral = 0
    for i in range(0,N):
        integral = integral + f((xpoints[i]+xpoints[i+1])/2)*h
    return integral

Nall = np.array([2, 4, 8, 16, 32])
error_T = []
error_M = []
for i in range(0,np.size(Nall)):
    N = Nall[i]
    h = (b-a)/N
    xpoints = np.linspace(a,b,N+1) 
    integral_T = Trapezoidal(h,N,xpoints)
    integral_M = Midpoint(h,N,xpoints)
    error_T_new= np.abs(integral_T-intexact)
    error_M_new = np.abs(integral_M-intexact)
    error_T.append(error_T_new)
    error_M.append(error_M_new)
    print('For h = ' +str(h))
    print('Error for trapezoidal rule is e_T = ' +str(error_T[i]))
    print('Error for midpoint rule is e_M = ' +str(error_M[i]))

hall = (b-a)/Nall

fig, (ax1) = plt.subplots(1,1)
ax1.plot(hall, error_T,label="Trapezoidal rule")
ax1.plot(hall, error_M,label="Midpoint rule")
ax1.legend(loc="lower right")
ax1.set_title("Errors")
ax1.grid(True)
 

plt.show()
plt.show()
plt.show()
