class Drink:
    def __init__(self,name:str,price:float, size:str):
        self.name= name
        self.price= price
        self.size= size

    def display_info(self):
        return f"{self.name}-{self.size}-{self.price} SAR"
    
    def change_price(self, new_price):
        self.price = new_price

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)


drink1= Drink("Latte",18,"Medium")
drink2= Drink("Espresso", 12,"small")
drink3= Drink("Cappuccino",22,"Large")
print("=== Coffee Shop Menu ===")
print(drink1.display_info())
print(drink2.display_info())
print(drink3.display_info())

drink1.change_price(20)
drink3.apply_discount(25)
print("-"*100)
print("=== Updated Menu ===")
print(drink1.display_info())
print(drink3.display_info())
                          
                          