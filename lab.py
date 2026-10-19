# Lab

class Drink:

    def __init__(self, name:str, size:str, price:float) -> None:
        self.name = name
        self.size = size
        self.price = price
        


    def display_info(self):
        display = f"{self.name} - ({self.size}) - {self.price} SAR"
        return display



    def change_price(self, new_price):
      self.price =  new_price 
      return new_price


    def apply_discount(self, percentage):
        discount = self.price *  (percentage / 100)
        final_price = self.price - discount
        return final_price
        


drin1 = Drink("Latte", "Medium", 18)
drin2 = Drink("Espresso", "Small", 12)
drin3 = Drink("Cappuccino", "Large", 22)


print("=== Coffee Shop Menu ===")
print(drin1.display_info())
print(drin2.display_info())
print(drin3.display_info())
print()
print("=== Updated Menu ===")
print(f"{drin1.name} ({drin1.size}) - {drin1.change_price(20)}")
print(f"{drin3.name} ({drin3.size}) - {drin3.apply_discount(25)}")
