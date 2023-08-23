import numpy as np

# Define function to be integrated
def f(x):
    f = np.exp(x)
    return f

# Define integral boundaries
a = 0
b = 1

# Define equidistant grid
N = 10
h = (b-a)/N
xpoints = np.linspace(a,b,N+1) # Note that we technically use N+1 points, since go from x0 to xN


# Calculate sum using midpoint rule
integral = 0
for i in range(0,N):
    integral = integral + f((xpoints[i]+xpoints[i+1])/2)*h
    

print(integral)

