from item import Item

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