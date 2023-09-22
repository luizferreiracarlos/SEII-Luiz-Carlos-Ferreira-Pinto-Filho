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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value

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
        return self.__price*self.quantity         # sempre passa o próprio objeto como parâmetro entre suas referências.

    def apply_discount(self):                   # Método para aplicar o desconto sobre o preço, baseado no atributo da classe.
        self.__price = self.__price*self.pay_rate   # O método usa uma referência de pay_rate a nível de instância para fazer o cálculo.
    
    def apply_increment(self, increment):                   # Método para aplicar o desconto sobre o preço, baseado no atributo da classe.
        self.__price = self.__price + self.__price*increment
    
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
                Hello everyone.
                We have {self.name} {self.quantity} times.
                Regards...
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"

    @property
    def read_only_name(self):
        return "TÃO BATUCANDO AQUI PERTO"