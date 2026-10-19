class Drink: 
    def __init__(self, name, price, size):

        self.name = name
        self.price = price
        self.size = size
    
    def __str__(self):

        return f"{self.name} - {self.price:.2f} SAR ({self.size})"
    
    def display_info(self):

        print(self)

    def change_price(self, new_price):

        self.price = new_price 

    def apply_discount(self, percentage):

        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount


print("===== Coffee Shop Menu ====")

Latte = Drink("Latte", 18.00, "Medium")
Latte.display_info()

Espresso = Drink("Espresso", 12.00, "Small")
Espresso.display_info()

cappuccino = Drink("Cappuccino", 22.00, "Large")
cappuccino.display_info()

print("="*30)
print("v v Updated Prices v v")
print("="*30)

Latte.change_price(20.00)
Latte.display_info()

cappuccino.apply_discount(25)
cappuccino.display_info()