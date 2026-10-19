class Drink:
    def __init__(self,name,price,size):
        self.name = name
        self.price = price
        self.size = size
    
    def display_info(self):
        print(F"{self.name}({self.size}) - {self.price} SAR")
    def change_price(self, new_price):
         self.price = new_price

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)


latte = Drink("Latte", 18, "Medium")
espresso = Drink("Espresso", 12, "Small")
cappuccino = Drink("Cappuccino", 22, "Large")

print("\n☕ = COFFEE SHOP MENU = ☕")
latte.display_info()
espresso.display_info()
cappuccino.display_info()

print("\n✨ == UPDATED MENU == ✨")

latte.change_price(20)
cappuccino.apply_discount(25)


latte.display_info()
cappuccino.display_info() 

print("\n☕ Thank you for visiting! ❤️")