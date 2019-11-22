import numpy as np
import pandas as pd
import random

df = pd.read_csv("renal_valores_numericos.csv")

for j in range(30): # Definimos el maximo numero de iteraciones del algoritmo
    n = df.values.shape[1]
    std = np.zeros(n)
    for i in range(n):
        std[i] = np.std(df.values[:, i]) # Se optienen las desviaciones estandar por columna

    similar_rows = {} # Se crea el diccionario para los vecinos cercanos
    m = df.values.shape[0]
    for i in range(m):
        similar_rows[i] = ([-1, -1, -1], [999, 999, 999])
        for k in range(m):
            # Se obtiene la distancia de mahalanobis
            mahalanobis = np.sqrt(np.sum(((df.values[i] - df.values[k])/std)**2))
            index, dist = similar_rows[i]

            if i != k and mahalanobis < dist[0]: # En caso de que 
                dist.pop(0)                     #  sea menor que la mayor 
                dist.append(mahalanobis)        # de los 3 vecinos se
                index.pop(0)                    # reemplaza
                index.append(k)
                similar_rows[i] = (index, dist)

    X = df.values

    for i in range(m):
        for k in range(n):
            if X[i,k] == -1: # Se buscan los valores faltantes denotados por un 0
                index, dist = similar_rows[i]
                # Se elige aleatoreamente uno de los tres vecinos mas proximos
                X[i,k] = X[index[random.randint(0,2)],k] 

    # Se imprime la iteracion en la que va el algoritmo y cuantos datos faltantes quedan por reemplazar
    print("Barrido no. {} , datos por completar: {}".format(j+1, np.count_nonzero(X==-1)))
    # Se hace una nuevo csv
    df = pd.DataFrame(X,columns=df.columns.values)
    name = 'completa_datos_prueba_3/renal_iteration_{}_no_faltantes_{}.csv'.format(j+1, np.count_nonzero(X==-1))
    pd.DataFrame(X,columns=df.columns.values).to_csv(name,index=False)
