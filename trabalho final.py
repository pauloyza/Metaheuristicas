#Steps expected for the program
#
# 1) Read the txt file and convert to a numpy matrix
# 2) Make a unique Grasp which will work according the entry to generate, in this case, 4 solutions (combinatory pf 2 contructives and 2 refinements methods)
# 3) Compare the results with each other, save these results for a report

# Grasp reativo
# A lrc tem que ter mais de um elemento
#Libraries
#from math import nextafter
import numpy as np
import random as rd
#(1)
matriz = np.loadtxt('five_d.txt') 
#print(matriz[1,3], type(matriz[0,1]))

#(2)
max_interactions = 5
matriz[matriz == 0] = np.nan
alpha = 1

global city_all 
global real_best_solution
global wall_hacker
city_all = len(matriz[0])
real_best_solution = np.array([])
wall_hacker= np.argsort(matriz)
def grasp(max_interactions):
    #making a array with the cities, we have to drop after each interaction

   
    cities = np.arange(0, city_all) # an array like [1,2,3, ... , last city]
    city_begin_arrays = np.array([])
    
    


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

        #construtor normal
        real_best_solution, better_distance = constructGuloso(better_solution, distance, better_distance)
        #print("melhor s ate entao:",real_best_solution," com d = ", better_distance)
        better_solution, distance = constructGuloso(better_solution, better_distance, better_distance, 1, alpha)
        #print("melhor s ate entao:",real_best_solution," com d = ", better_distance)
        
        #Saving the best solution if it's true
        #if ( (better_distance == 0) | (distance < better_distance) ):
        #    better_distance = distance
        #    real_best_solution = better_solution
    return real_best_solution, better_distance
    #começar aqui a puxar a busca local          

def constructGuloso(better_solution, distance, better_distance, bias = 0, alpha = 1):
    print("melhor s ate entao:",real_best_solution," com d = ", better_distance)
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
            
            distance = getDistance(better_solution)              
        else:
            break#mudar isso
    
    if((bias == 1) | (bias == 2)):
        #case final, the last one
        print("melhor s ate entao:",real_best_solution," com d = ", better_distance)
        if (city_all - len(better_solution) == 1):
            #choose the last city
            #print("new:",better_solution," ",distance)
            last_city = getRest(better_solution)
            better_solution = np.append(better_solution, last_city)
            distance = getDistance(better_solution)
            return better_solution, distance

        #case almost final, here there 2 cities yet. Here we're gonna use the bias
        elif (city_all - len(better_solution) == 2):
            #print("new:",better_solution," ",distance)
            lrc = getRest(better_solution) #lrc of 2 itens
            if bias == 1:
                #print("new:",better_solution," ",distance)
                index = rd.randint(0,1)
                better_solution, distance = constructGuloso( np.append(better_solution, int(lrc[index])), distance, better_distance, 1, alpha )

            if bias == 2:
                b_a, d_a = constructGuloso(np.append(better_solution, lrc[0]), distance, better_distance, 2, alpha)
                b_b, d_b = constructGuloso(np.append(better_solution, lrc[1]), distance, better_distance, 2, alpha)
                
                better_solution = b_a if d_a<d_b else b_b
        else:
            #Calculate of the values in alpha WE GOTTA HAVE TWO VALUES AT LEAST
            print("meudeus: ",better_solution)
            lrc = getLRC(better_solution, alpha)
            #print("lrc: ",lrc[index])
            print("LRC verdadeira: ",lrc)
            if bias == 1:
                #print("new2:",better_solution," ",distance)
                index = rd.randint(0, len(lrc)-1)
                print("INDEX EH:", lrc[index])
                #print("lrc: ",lrc[index])
                better_solution, distance = constructGuloso(np.append(better_solution, int(lrc[index])), distance, better_distance, 1, alpha)
                #print("oioi")

            if bias == 2:
                for i in lrc:
                    b_a, d_a = constructGuloso(np.append(better_solution, i, distance, better_distance,2,alpha))
                    if d_a < distance:
                        better_solution = b_a               


    #print("Teste final: sol:",better_solution," e distan:",distance)
    return better_solution, distance

#Aux function
def getDistance(better_solution):
    solution_aux = np.append(better_solution, better_solution[0])    
    distance = 0
    for ii in range(len(better_solution)):
         distance += matriz[solution_aux[ii]][solution_aux[ii+1]]   

    return distance         

def getRest(better_solution):
    return np.argwhere( (np.in1d( np.arange(1, city_all +1), better_solution )) == False )

def getLRC(better_solution, alpha):
    interrupt = 1
    lrc = np.array([])
    #print(wall_hacker)
    #if(len(better_solution)==1):
    #    return lrc
    for next_city in wall_hacker[better_solution[-1]]:
        print(lrc)
        #print("next_c:", next_city)
        if ((np.any(better_solution != next_city)) & (interrupt == 1)):
            #tolerance = best distance + [(worst distance - best distance) * alpha]
            #print("interrupt:",interrupt)
            best_distance   = matriz[better_solution[-1]][next_city]
            worst_distance  = matriz[better_solution[-1]][wall_hacker[better_solution[-1]][-2]]
            tolerance = float(best_distance) + ((float(worst_distance) - float(best_distance)) * alpha)
            lrc = np.append(lrc, next_city)
            interrupt = 0
            #print(tolerance)
            #print('oi')
            continue

        if ((interrupt == 0) & (len(lrc) == 1)):
            print('oii')
            #If the distance of the next element is bigger than the tolerance and there's only one element into the lrc, get this element and stop ALL
            if( (float(matriz[better_solution[-1]][next_city])) > tolerance ):
                #print('oiii')
                lrc = np.append(lrc, next_city)
                break

            else:
                lrc = np.append(lrc, next_city)

        elif ((interrupt == 0) & (float(matriz[better_solution[-1]][next_city]) <= tolerance ) ):
            #print("tchau")
            lrc = np.append(lrc,next_city)

                

    return lrc
s, r = grasp(max_interactions)
print(matriz)

#a = getLRC(np.asarray([1]),0.1)
#print(a)

print("solution final:", s, "com distancia = ",r)

