import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculateTotalPrice(self):              # Método da classe para retornar a soma de inteiros. O parâmetro self sempre deve ser colocado, uma vez que o python.
        return self.price*self.quantity         # sempre passa o próprio objeto como parâmetro entre suas referências.

    def apply_discount(self):                   # Método para aplicar o desconto sobre o preço, baseado no atributo da classe.
        self.price = self.price*self.pay_rate   # O método usa uma referência de pay_rate a nível de instância para fazer o cálculo.
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        pass

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Usando a função super para ter acesso a todos os atributos/metodos.
        super().__init__(
            name, price, quantity
        )

        # Checando se as variáveis recebidas como parâmetro são valores positivos. Caso não sejam é acusado um assert error e a mensagme da fstring é exibida
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than zero!"
 
        # Assinando as variáveis recebidas pelo construtor.
        self.broken_phones = broken_phones
        pass

phone1 = Phone('jscPhonev01', 500, 5, 1)

print(Item.all)
print(Phone.all)