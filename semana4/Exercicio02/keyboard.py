from item import Item

class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity=0):
        # Usando a função super para ter acesso a todos os atributos/metodos.
        super().__init__(
            name, price, quantity
        )
    pass