import numpy as np 

a = np.array([[1,2], [3,4], [5,6]])
print(a)

bool_idx = a > 2    #Salva True para valores de a maior que 2 e False para os demais
print(bool_idx)
print(a[bool_idx])  #Cria um vetor apenas com os valores maior que 2

b = np.where(a>2, a, -1) #Cria um vetor de mesma dimensao que a com os respectivos 
#valores onde e maior que 2, e os que sao menores coloca-se 1 no lugar
print(b)

c = np.array([10,19,30,41,50,61])
d = [1,3,5]
print(c[d]) #Printa apenas os valores de c com o index dos vetores contidos em `d`