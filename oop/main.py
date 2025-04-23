from item import Item
from phone import Phone
import pandas as pd

# More about getter and setters
# How to restict user from editing few read only attributes
# How to use "encapsulation"
# Item.instantaliate_from_dataframe()
# print(Item.all)
item1 = Item("myItem", 500, 5)
print(item1.name)

item1.name = "otherItem" #execute the setter

print(item1.name) # where ever you will use name it will execute proporty decorator

item1.price = -9000

print(item1.price)