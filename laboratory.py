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
#print(matriz)
#print(np.argsort(matriz))
#x = np.arange(24).reshape((2, 3, 4))
#print(x)
#print(np.argm()))

#city_all = len(matriz[0])
#print(city_all)
#cities = np.arange(0, city_all)
#print(cities)

array_uai = np.arange(1,5)
array_normal = np.arange(1,6)
print(array_uai)
print(array_normal)

array_bool = np.in1d(array_normal, array_uai)
print(array_bool)
print(np.argwhere(array_bool == False))
array_uai[-1]

print(np.any(array_uai == 3))