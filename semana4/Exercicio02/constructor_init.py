
#item1 = 'Phone'
#item1_price = 100
#item1_quantity = 5
#item1_price_total = item1_price*item1_quantity



class Item:     # Criando a classe Item para registrar os dados relacionados.
    # Variáveis globais para a classe
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Checando se as variáveis recebidas como parâmetro são valores positivos. Caso não sejam é acusado um assert error e a mensagme da fstring é exibida
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
 
        # Assinando as variáveis recebidas pelo construtor.
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

        pass                                    
    def calculateTotalPrice(self):              # Método da classe para retornar a soma de inteiros. O parâmetro self sempre deve ser colocado, uma vez que o python.
        return self.price*self.quantity         # sempre passa o próprio objeto como parâmetro entre suas referências.
        pass

    def apply_discount(self):                   # Método para aplicar o desconto sobre o preço, baseado no atributo da classe.
        self.price = self.price*self.pay_rate   # O método usa uma referência de pay_rate a nível de instância para fazer o cálculo.
        pass
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        pass


item1 = Item("Phone", 100, 5)              # Criando a primeira instância item com seus dados relacionados.
item2 = Item("Laptop", 1000, 3)            # Criando a segunda instância item com seus dados relacionados.
item2.pay_rate = 0.7                # Atualizando a porcentagem de desconto.
item2.is_numpad =  False            # Posso criar atributos novos para a classe mesmo após criar suas instâncias.
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)



print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.calculateTotalPrice())
print(item2.calculateTotalPrice())
print(Item.__dict__)                    # Print de todos os atributos da classe
print(item1.__dict__)                   # Print de todos os atributos da instância

item1.apply_discount()
item2.apply_discount()
print(f'\nRecalculated price (1): {item1.price}')
print(f'Recalculated price (2): {item2.price}')

print(Item.all)