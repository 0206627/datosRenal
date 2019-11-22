import numpy as np
import pandas as pd


df = pd.read_csv("valores_cuantitativos.csv")

n = df.values.shape[1]
X = df.values
for i in range(n):
    idx = X[:,i]=='?'
    X[idx,i] = -1

pd.DataFrame(X,columns=df.columns.values).to_csv('renal_valores_numericos.csv',index=False)