import numpy as np

a = np.array([[1,2,6], [3,4,8]])
print(a)
print(a.shape)
print(a[0][0]) #Printa o primeiro elemento da primeira linha e primeira coluna
print(a.T) # Transposta de `a`

b = np.array([[1,2],[3,4]])
print(np.linalg.det(b)) #Calcula o determinante 
print(np.diag(b))   # Calculo da diagonal
