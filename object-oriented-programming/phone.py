from item import Item
import pandas as pd

class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0) -> None:
        # call to super function to access to all attributes and methods
        # I am not sure what method we are talking about?
        super().__init__(
            name, price, quantity
        )
        # Run validation to the received arguments
        assert broken_phones >=0, f"brokenphones {broken_phones} is not greater than or equal to zero"
        # Assign values to the attributes/self object
        self.broken_phone = broken_phones