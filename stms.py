class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        # validating the recieved arguments
        
        
    def calc_total_price(self):
        return self.price * self.quantity

item_1 = Item("Phone", 100, 5)

item_2 = Item("Laptop", 1000, 8)


print(item_2.calc_total_price())