from drink import Drink

latte = Drink("Latte", "Medium", 18)
espresso = Drink("Espresso", "Small", 12)
cappuccino = Drink("Cappuccino", "Large", 22)

print("=== Coffee Shop Menu ===")
latte.display_info()
espresso.display_info()
cappuccino.display_info()

latte.change_price(20)
cappuccino.apply_discount(25)

print("\n=== Updated Menu ===")
latte.display_info()
cappuccino.display_info()