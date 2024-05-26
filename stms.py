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
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
       
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
        return f"Item'{self.name}, {self.price}, {self.quantity}'"
  

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call on super function to access all attributes/methods from the parent function
        super().__init__(
            name, price, quantity
        )
        
        # validating the recieved arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to  zero"

        # Assigning attributes to self object
        self.broken_phones = broken_phones
        
        #actions to execute
        Phone.all.append(self)

  
phone_1 = Phone("iphone15", 500, 5)
print(phone_1.calc_total_price())
phone_2 = Phone("iphone11", 600, 4)




    

#the __dict__ magic attribute brings all the attributes at the class and instance level
# when a class method is called, the class is passed as the first argument 
# static method is not specific to any object so the static method can be defined outside the class as a function


    

    

