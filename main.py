class Drink:
    def __init__(self,name,price,size):
             self.name = name
             self.price = price
             self.size = size               
    
       
        

    def display_info(self):
                print(f"{self.name} ({self.size}) - {self.price} SAR")
    def change_price(self , New_price):
                self.price = New_price
    def apply_Discount(self , percentage):
                self.price = self.price - (self.price * percentage / 100)

               

latte = Drink("Latte", 18, "Medium")
espresso = Drink("Espresso", 12, "Small")
cappuccino = Drink("Cappuccino", 22, "Large")


print("=== Coffee Shop Menu ===")
latte.display_info()
espresso.display_info()
cappuccino.display_info()

latte.change_price(20)
cappuccino.apply_Discount(25)

print("=== Updated Menu ===")
latte.display_info()
cappuccino.display_info()


