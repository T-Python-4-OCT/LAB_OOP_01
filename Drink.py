class Drink:

    def __init__(self, name:str, size:str, price:int):
        self.name = name
        self.size = size
        self.price = price

    def display_info(self):
        insert = f"{self.name} ({self.size}) - {self.price} SAR"
        print(insert)

    def change_price(self, new_price):
        self.price = new_price
        return new_price

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)
        return percentage

        
# Create Opjects
First_drink = Drink("V60", "Medium", 18)
Second_drink = Drink("Espresso", "Small", 12)
Third_drink = Drink("Latte", "Large", 20)

# Display menu
print("=== Coffee Shop Menu ===")
First_drink.display_info()
Second_drink.display_info()
Third_drink.display_info()

# Change price & Discount
First_drink.change_price(20)
Third_drink.apply_discount(25)

# Update 
print("=== Updated Menu ===")
First_drink.display_info()
Third_drink.display_info()