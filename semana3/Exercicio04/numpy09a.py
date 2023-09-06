import numpy as np 

a = np.arange(1,7)
print(a)
b = a[np.newaxis, :] #Cria uma lista de listas
print(b)