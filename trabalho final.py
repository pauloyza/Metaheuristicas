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
matriz[matriz == 0] = np.nan
def grasp(max_interactions):
    #making a array with the cities, we have to drop after each interaction
    global city_all 
    global real_best_solution
    global wall_hacker
    city_all = len(matriz[0])
    cities = np.arange(0, city_all) # an array like [1,2,3, ... , last city]
    city_begin_arrays = np.array([])
    real_best_solution = np.array([])
    wall_hacker= np.argsort(matriz)


    #Finding the "best" solution only with the greedy method
    for i in range(max_interactions):
        #Start the construct method

        #a) chose a random start possible city
        while (1):
            city_begin = rd.randint(0, city_all-1)
            if not (np.any(city_begin_arrays == city_begin)):
                break
        #b) feeding the array
        city_begin_arrays = np.append(city_begin_arrays, np.asarray(city_begin))
        
        #cities_aux = np.delete(np.arange(1, city_all+1), x)
        #cities_aux = matriz[x]
        
        #c) making the first rote
        better_distance = 0
        distance = 0
        better_solution = np.array(np.asarray([city_begin]))
        better_solution, distance = constructGuloso(better_solution, distance, better_distance)
        
        print("distancia:", distance, " best solution:", better_solution)
        #Saving the best solution if it's true
        if ( (better_distance == 0) | (distance < better_distance) ):
            better_distance = distance
            real_best_solution = better_solution
              

def constructGuloso(better_solution, distance, better_distance, bias = 0, alpha = 1):
    #bias 0 -> guloso normal
    #bias 1 -> local search random
    #bias 2 -> local search 
    while ( len(better_solution) < city_all ):
        #print(better_solution)
        if(bias == 0):
            for ii in range(city_all):
                    for j in wall_hacker[better_solution[-1]]:
                        if not ( np.any(better_solution == j) ):
                            better_solution = np.append(better_solution, j)
            solution_aux = np.append(better_solution, better_solution[0])    
                        
            for ii in range(len(better_solution)):
                distance += matriz[solution_aux[ii]][solution_aux[ii+1]]            

            
        else:
            break#mudar isso
    
    if((bias == 1) | (bias == 2)):
        #case final, the last one
        if (city_all - len(better_solution) == 1):
            print("oi")
            

    return better_solution, distance



grasp(max_interactions)
print(matriz)