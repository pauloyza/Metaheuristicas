from unittest import TextTestRunner
import numpy as np
import random as rd

#area de laboratorio
a = np.array([2,3,3])
b = np.array([1,4,5])

c = [1.2]
c = np.asarray(c)
print(type(c))
sabedor = np.any(a == 10)
print(sabedor)
matriz = np.loadtxt('five_d.txt') 
#print(matriz)
matriz[matriz == 0] = np.nan    
print(matriz)
print(np.argsort(matriz))
#x = np.arange(24).reshape((2, 3, 4))
#print(x)
#print(np.argm()))