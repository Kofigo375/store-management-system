import csv

class Item:
    pay_rate = 0.8 # discount after 20% discount
    all = list()
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is negative"
        assert quantity >= 0, f"quantity {quantity} is negative"

        # Assignment of attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity 

        # Actions to execute:
        Item.all.append(self)
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


    def calculate_total_price(self):
        return self.price * self.quantity

    def add_discount(self):
        self.price = self.price * self.pay_rate
    # creating a class method to instantiate objectes from the csv file
    @classmethod
    def instance_from_csv(cls):
        with open('Items.csv', 'r') as handle:
            reader = csv.DictReader(handle)  # read the content as list of dictionaries
            items = list(reader)
        for item in items:
            print(item)
            Item(
                name=item.get('Name'),
                price=float(item.get('Price')),
                quantity=int(item.get('quantity')),      
            )
    @staticmethod
    def is_int(some_num):
        if isinstance(some_num, float):
            return some_num.is_integer()  # ignoring floats that ends with .0 eg: 2.0, 4.0 etc
        elif isinstance(some_num, int):
            return True
        else:
            return False

class Phone(Item):
    pass


phone1 = Item("iphone_X", 2000, 12)
phone1.broken = 6
phone2 = Item("samsumg_s21", 2300, 10)
phone2.broken = 5

# revisit project after reviewing git commands






