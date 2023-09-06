import numpy as np 

l = [1,2,3]
a = np.array([1,2,3])

# Adicionando um 4 elemento
l = l+[4]
print(l)
# Duplicando a os valores da lista
l = l *2
print(l)
a = a + np.array([4]) #Soma 4 a cada indice da lista `a`
print(a)

# Multiplicando uma lista np array
a = a *2
print(a)

# Retirando a raiz de quadrada do meu np array
a = np.sqrt(a)
print(a)

# log 
a = np.log(a)
print(a)
