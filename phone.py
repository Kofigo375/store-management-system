from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call on super function to access all attributes/methods from the parent function
        super().__init__(
            name, price, quantity
        )
        
        # validating the recieved arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to  zero"

        # Assigning attributes to self object
        self.broken_phones = broken_phones
        