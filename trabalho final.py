#Steps expected for the program
#
# 1) Read the txt file and convert to a numpy matrix
# 2) Make a unique Grasp which will work according the entry to generate, in this case, 4 solutions (combinatory pf 2 contructives and 2 refinements methods)
# 3) Compare the results with each other, save these results for a report

# Grasp reativo
# A lrc tem que ter mais de um elemento
#Libraries
import numpy as np
import random as rd
#(1)
matriz = np.loadtxt('five_d.txt') 
#print(matriz[1,3], type(matriz[0,1]))

#(2)
max_interactions = 5
alpha = 0.2
print(matriz)
def grasp(max_interactions):
    #making a array with the cities, we have to drop after each interaction
    city_all = len(matriz[0])
    cities = np.arange(1, city_all+1) # an array like [1,2,3, ... , last city]
    city_begin_arrays = np.array([])
    #print(city_all)
    for i in range(max_interactions):
        #Start the construct method

        #a) chose a random start possible city
        while (1):
            city_begin = rd.randint(1, city_all)
            if not (np.any(city_begin_arrays == city_begin)):
                break
        #b) feeding the array
        city_begin_arrays = np.append(city_begin_arrays, np.asarray(city_begin))
        
        #cities_aux = np.delete(np.arange(1, city_all+1), x)
        #cities_aux = matriz[x]
        
        #c) making the first rote
        distance = 0
        better_solution = np.array(np.asarray(city_begin))
        better_solution, distance = contruct_guloso(city_begin)
        #c) choosing a way better with a for
        
        #print(better_solution)
        for i in range(len(cities_aux)):
            
            #next_city = np.amin(np.delete(cities_aux, np.where(cities_aux == 0))) #find the city next to (it's the distance)
            next_city = np.amin(np.array(cities_aux)[cities_aux != np.amin(cities_aux)]) #find the city next to (it's the distance)
            distance = distance + next_city #incrementa a distancia
            index__next_city = np.where(cities_aux == next_city)
            better_solution = np.append(better_solution, [cities_aux[index__next_city]])

            cities_aux = np.delete(cities_aux, index__next_city)
            #print("Se a cidade inicial eh: ", x+1, ", entao a melhor rota eh: ", better_solution)                

        #print("Se a cidade inicial eh: ", x+1, ", entao a melhor rota eh: ", better_solution)            

def construct_guloso(city_begin):
    
    return better_solution, distance



grasp(max_interactions)