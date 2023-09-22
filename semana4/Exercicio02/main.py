from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 750, 5)

item1.apply_discount()
print(item1.price)