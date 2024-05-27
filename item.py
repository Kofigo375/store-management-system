import csv

class Item:
    # class attributes belongs to the class and are common to all instances and can be assesed at the instance level
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # validating the recieved arguments
        assert price >= 0, f"Price {price} is not positive or equal to zero"
        assert quantity >= 0, f"Quanatity {quantity} is not greater than or equal to  zero"
        
        
        # Assigning attributes to self object
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

                 
    def calc_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate  
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('Items.csv', 'r') as f:
            reader = csv.DictReader(f)   ## this .DictReader reads our file as a list of dictionaries
            items = list(reader)
        for item in items:
            Item(
                name=item.get('Name'),
                price=float(item.get('Price')),
                quantity=int(item.get('quantity'))
            )  
            
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
         
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}'{self.name}, {self.price}, {self.quantity}'"
    

  