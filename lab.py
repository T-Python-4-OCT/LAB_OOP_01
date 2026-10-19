
class Drink:
    def __init__(self,name:str,price:float,size:str):
        self.name=name
        self.price=price
        self.size=size
        
    def display_info(self):
        info=f"{self.name} ({self.size}) - {self.price} SAR"
        return info
    
    def chang_pric(self,new_price):
       self.price=new_price
       
    def apply_discount(self,persintg):
        self.price=self.price-(self.price*persintg/100)
        
    
drink1=Drink("Latte",18,"Meduium")
drink2=Drink("Espresso ",12,"Small")
drink3=Drink("Cappuccino ",22,"Large")

print("=== Coffee Shop Menu ===")
print(drink1.display_info())
print(drink2.display_info())
print(drink3.display_info())

drink1.chang_pric(20)
drink3.apply_discount(25)

print("\n=== Updated Menu ===")
print(drink1.display_info())
print(drink3.display_info())