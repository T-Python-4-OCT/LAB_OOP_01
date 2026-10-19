class Drink:
    def __init__(self , name:str , price:float , size:str)->None:

        self.name = name
        self.price = price
        self.size = size

    def display_info (self):
        information = f" | {self.name}      | {self.size} | {self.price} SAR |"
        return information

    def change_price (self,new_price):
        self.price = new_price
        return new_price
    def apply_discount(self,percentage):
        discount_amount = self.price * (percentage / 100)
        self.price = self.price - discount_amount        


drink1 = Drink("Latte",18,"Medium")
drink2 = Drink("Espresso",12,"Small")
drink3 = Drink("Cappuccino",22,"Large")

print("=== Coffee Shop Menu ===")

print("| Name       | Size   | Price  |")
print ("| ---------- | ------ | ------ |")
print (drink1.display_info())
print (drink2.display_info())
print (drink3.display_info())

drink1.change_price(20)
drink3.apply_discount(25)


print("=== Updated Menu ===")
print("| Name       | Size   | Price  |")
print ("| ---------- | ------ | ------ |")
print (drink1.display_info())
print (drink2.display_info())
print (drink3.display_info())
