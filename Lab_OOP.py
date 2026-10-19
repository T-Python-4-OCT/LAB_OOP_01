
class Drink:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def display_info(self):
        print(f"{self.name} ({self.size}) - {self.price:g} SAR")

    def change_price(self, new_price):
        self.price = new_price

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)


# Create drink objects
latte = Drink("Latte", 18, "Medium")
espresso = Drink("Espresso", 12, "Small")
cappuccino = Drink("Cappuccino", 22, "Large")



# Display the original menu
print("=== Coffee Shop Menu ===")
latte.display_info()
espresso.display_info()

cappuccino.display_info()

# Update prices
latte.change_price(20)
cappuccino.apply_discount(25)



# Display the updated menu
print("\n=== Updated Menu ===")
latte.display_info()
cappuccino.display_info()
