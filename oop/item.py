import pandas as pd

class Item:
    pay_rate = 0.8 # class level attribute
    all = []
    item_dict = {
        "name": ["Phone", "Laptop", "Cable", "Mouse", "Keyboard"],
        "price": [100, 1000, 10, 50, 75],
        "quantity": [1,3,5,5,5]
    }
    # Any method called in a class take atleast one paramter that is self
    # Magic methods: constructors
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        # Run validation to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        # Assign values to the attributes/self object
        # First we will assign the value to name
        # self.name = name
        # Second, we want to make 'name' readable by using property, so modidied the actual name to '_name'
        # self._name = name
        # Lastly, make name private so that it won't be accesible outside class, use __name
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Executable instances
        Item.all.append(self)
    
    @property
    def name(self):
        # property decirator, name is not a method but a readable attribute
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            print("name is too long")
        else:
            self.__name = value
    
    def get_total_price(self):
       return self.quantity * self.price
    
    def get_discounted_price(self):
        return self.price*self.pay_rate
    
    @classmethod
    def instantaliate_from_dataframe(cls):
        df = pd.DataFrame(Item.item_dict)
        dict_list = []
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            row_dict = row.to_dict()   # Convert the row to a dictionary
            dict_list.append(row_dict) # Append the dictionary to the list
        
        for item in dict_list:
            Item(
                name = item.get("name"),
                price = item.get("price"),
                quantity = item.get("quantity")
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"
    
    # this was used just to see how a property decorator works
    # @property
    # def read_only_name(self):
    #    return "AAA"