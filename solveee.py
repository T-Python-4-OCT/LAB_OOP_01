class Drink:
    def __init__(self,name,price,size):
        self.name=name
        self.price=price
        self.size=size
        
        
    def display_info(self):
        print(f"{self.name} ({self.size}) - {self.price} SAR")    


    def change_price(self,new_price):
         self.price=new_price
        
        
    def apply_discount(self,perCen):
        self.price=self.price * (1-perCen /100)
    
    
    
    
latte=Drink("Latte",18,"Medium")
Espresso=Drink("Espresso",12,"Small")
Cappuccino=Drink("Cappuccino",22,"Large")

print("COFFEESHOP MENU")
latte.display_info()
Espresso.display_info()
Cappuccino.display_info()


latte.change_price(20)
Cappuccino.apply_discount(25)

print("Updated MENU:")
latte.display_info()
Cappuccino.display_info()
