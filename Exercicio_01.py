from asyncio.windows_events import NULL
import numpy as np

semente = input("Escreva um inteiro para ser a semente:")
aleatorio = np.random.default_rng(seed = int(semente))

aleatorio_inteiros = np.empty([10,100])

#criando o arquivo texto
arquivo = open('arq01.txt','w')

for i in range(10):
    x = aleatorio.integers(low=0, high=1000, size=100)  
    aleatorio_inteiros[i] = x #Etapa para guardar esse array em um ndarray, que posteriormente pode ser útil

    #Converter o x para uma string e escreve no arquivo
    x_linha = " ".join([str(elem) for elem in x.tolist()])
    arquivo.write(x_linha + '\n')

arquivo.close()

print(aleatorio_inteiros)