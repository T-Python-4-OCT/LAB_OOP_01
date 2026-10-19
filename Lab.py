class Drink :
    def __init__(self, name, size, price):
        self.name = name
        self.price = price
        self.size = size

    def display_info(self) :
        print(self.name, f"({self.size})",'-', self.price, 'SAR')
        
    def change_price(self, new_price) :
        self.price = new_price
    
    def apply_discount(self, percentage) :
        discount = self.price * percentage/100
        self.price = self.price - discount

D1 = Drink('Latte', 'Medium', 18)
D2 = Drink('Espresso', 'Small', 12)
D3 = Drink('Cappuccino', 'Large', 22)

print(f"\n=== Coffee Shop Menu ===\n")
D1.display_info()
D2.display_info()
D3.display_info()

D1.change_price(20)
D3.apply_discount(25)
print(f"\n=== Updated Menu ===\n")
D1.display_info()
D3.display_info()
