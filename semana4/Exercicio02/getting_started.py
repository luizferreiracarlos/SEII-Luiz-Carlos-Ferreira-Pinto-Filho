
#item1 = 'Phone'
#item1_price = 100
#item1_quantity = 5
#item1_price_total = item1_price*item1_quantity



class Item:                                     # Criando a classe Item para registrar os dados relacionados.
    def calculateTotalPrice(self, x, y):        # Método da classe para retornar a soma de inteiros. O parâmetro self sempre deve ser colocado, uma vez que o python
        return x*y                              # sempre passa o próprio objeto como parâmetro entre suas referências.
        pass

item1 = Item()              # Criando o primeiro item com seus dados relacionados.
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

print(item1.calculateTotalPrice(item1.quantity, item1.price))       # Usando o método da classe para calcular o preço total baseado em sua estrutura de dados.

item2 = Item()              # Criando o segundo item com seus dados relacionados.
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

print(item1.calculateTotalPrice(item2.quantity, item2.price))