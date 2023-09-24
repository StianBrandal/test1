import numpy as np

A = np.array([[1,1,1,1,1],[11,7,5,13,0],[21,23,10,11,35],[0,5,15,20,25],[12,0,23,17,13]])
#B = np.array([500,2550,11725,8750,6025])
B = np.array([[500],[2550],[11725],[8750],[6025]])
print(A)
print(B)
result =np.linalg.solve(A,B)
print(np.rint(result).flatten())