#! C:\Users\stian\OneDrive\Documents\Skule\ADA501 Matematisk modellering og simulering\Code\myenv\Scripts\python.exe
import numpy as np

# Define lengths
L12 = 0.3
L23 = 0.3
L24 = 0.4
L34 = 0.5
L35 = 0.4
L45 = 0.3
L56 = 0.3

# Entry and exit pressures for p1 and p6
pentry = 1
pexit = 0

# Construct linear system of equations
A = np.array([[1, 0, 0, 0, 0, 0],
              [1/L12, -(1/L12 + 1/L23 + 1/L24), 1/L23, 1/L24, 0, 0],
              [0, 1/L23, -(1/L23 + 1/L34 + 1/L35), 1/L34, 1/L35, 0],
              [0, 1/L24, 1/L34, -(1/L24 + 1/L34 + 1/L45), 1/L45, 0],
              [0, 0, 1/L35, 1/L45, -(1/L35 + 1/L45 + 1/L56), 1/L56],
              [0, 0, 0, 0, 0, 1]])
b = np.array([[pentry], [0], [0], [0], [0], [pexit]])

# Solve linear system
p = np.linalg.solve(A, b)

print(p)

# Calculate the flow rates
q12 = (p[0]-p[1])/L12
q23 = (p[1]-p[2])/L23
q24 = (p[1]-p[3])/L24
q34 = (p[2]-p[3])/L34
q35 = (p[2]-p[4])/L35
q45 = (p[3]-p[4])/L45
q56 = (p[4]-p[5])/L56
print()
print()
print(q12)
print(q23)
print(q24)
print(q34)
print(q35)
print(q45)
print(q56)
print("code is finished!!!")
