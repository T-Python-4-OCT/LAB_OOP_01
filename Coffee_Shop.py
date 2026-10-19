
class Drink:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def display_info(self):
        print(f"{self.name} ({self.size}) - {self.price} SAR")

    def change_price(self, new_price):
        self.price = new_price

    def apply_discount(self, percentage):
        self.price *= (1 - percentage / 100) # 22 * (1 - 25 / 100) = 16.5 

latte = Drink("Latte", "Medium", 18)
espresso = Drink("Espresso", "Small", 12)
cappuccino = Drink("Cappuccino", "Large", 22)

print("========= Coffee Shop Menu ========")
latte.display_info()
espresso.display_info()
cappuccino.display_info()

latte.change_price(20)
cappuccino.apply_discount(25)

print("\n========= Updated Menu ============")
latte.display_info()
cappuccino.display_info() 