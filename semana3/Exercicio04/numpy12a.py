import numpy as np

a = np.array([[7,8,9,10,11,12,13,14],[15,16,17,18,19,20,21,22]])
print(a)
print(a.sum(axis = 0)) #Somatorio das colunas
print(a.sum(axis = 1)) # Somatorio das linhas
print(a.mean(axis = None)) 
print(a.var(axis=None))