# ROTATE AN M x M ARRAY BY 90 DEGREES TO THE RIGHT
import numpy as np

size = 4 # matrix dimension
m1 = np.random.randint(1,10, size = (size, size)) # initializing a random array
m2 = np.zeros_like(m1) # auxilliary array of the same size as given array

print(f"Original Array : \n{m1}")

i,j = 0, m1.shape[1]-1 # start indices

while i<m1.shape[0] and j<m1.shape[1]:
    m2[:, j] = m1[i, :]
    # print('now : \n',m2)
    m2[j, :] = m1[:, j][::-1]
    # print('now : \n',m2)
    
    m2[:, i] = m1[j, :]
    # print('now : \n',m2)
    m2[i, :] = m1[:, i][::-1]
    # print('now : \n',m2)
    i+=1
    j-=1
    
    if i == j:
        m2[i, j] = m1[i, j]
        break

print(f"Rotated Array : \n{m2}")