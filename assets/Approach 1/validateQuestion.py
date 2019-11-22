
##################
# Código para inferir valores numéricos incompletos

import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

df = pd.read_csv("renal.csv")

X = df.values
num_var = [0,1,2,3,4,9,10,11,12,13,14,15,16,17]

minActual = [1000000]*len(num_var)
min = 10000

for r in range(400):
    for c in num_var:
        if df.values[r,c] != '?':
            continue
        for r2 in range(400):
            if r2 != r:
                aux = []
                for c2 in num_var:
                    if c2 != c:
                        renglon = df.values[:, c2]
                        renglon = renglon[renglon != '?']
                        desv = statistics.stdev(renglon.astype(float))
                        #print(desv)

                        a = float(df.values[r,c2]) if df.values[r,c2] != '?' else desv*100
                        b = float(df.values[r2,c2]) if df.values[r2,c2] != '?' else a*100

                        dif = abs(a-b)/desv
                        aux.append(dif)

                if sum(minActual) > sum(aux):
                    minActual = aux
                    min = r2
        df.values[r,c] = df.values[min,c]
        print("nuevo renglón:", df.values[r,:])

pd.DataFrame(X,columns=df.columns.values).to_csv('renal_imp.csv',index=False)