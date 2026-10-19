
class Drink:

    def __init__(self, name:str, price:float, size:str) -> None:

        self.name = name
        self.price = price
        self.size = size

    def display_info (self):
        print(f"{self.name} ({self.size}) - {self.price} SAR")

    def change_price(self, new_price):
        self.price = new_price

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price = self.price - discount_amount


latte = Drink("Latte", 18, "Medium")
espresso  = Drink("Espresso", 12, "Small")
cappuccino  = Drink("Cappuccino", 22, "Large")


print("=== Coffee Shop Menu ===")
latte.display_info()
espresso.display_info()
cappuccino.display_info()

latte.change_price(20)
cappuccino.apply_discount(25)

print()
print("=== Updated Menu ===")
latte.display_info()
cappuccino.display_info()