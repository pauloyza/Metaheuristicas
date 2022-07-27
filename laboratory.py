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
matriz[matriz == 0] = np.nan
print(matriz)
matriz[matriz == 0] = np.nan    
print(matriz)
wall_hacker = np.argsort(matriz)
print(wall_hacker)

x=3
distance = 0
vector = np.asarray([x])
print(vector[-1])
for i in range(5):
    for j in wall_hacker[vector[-1]]:
        if not(np.any(vector == j)):
            vector = np.append(vector, j)
vector_aux = np.append(vector, vector[0])
for i in range(len(vector)):
    distance += matriz[vector_aux[i]][vector_aux[i+1]]

#print("distancia: ",distance)
#print(vector)
#print(matriz)            
#x = np.arange(24).reshape((2, 3, 4))
#print(x)
#print(np.argm()))

#city_all = len(matriz[0])
#print(city_all)
#cities = np.arange(0, city_all)
#print(cities)

array_uai = np.asarray([2,4,3])
array_normal = np.asarray([0,1,2,3,4])
print(array_uai)
print(array_normal)
print(np.in1d( array_normal, array_uai) )
last_city = np.argwhere( (np.in1d( array_normal, array_uai )) == False )
print("aqui ",rd.randint(0,1))
array_bool = np.in1d(array_normal, array_uai)
#print(array_bool)
#print(np.argwhere(array_bool == False))
array_uai[-1]

#print(np.any(array_uai == 3))

asa = np.array([[]])
#print(type(asa))

#alet = rd.randint()