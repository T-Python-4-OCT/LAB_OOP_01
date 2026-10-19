class Drink:
  def __init__(self, name, size, price):
    self.name = name
    self.size = size
    self.price = price

  def display_info(self):
    print(f"{self.name} ({self.size}) - {self.price} SAR")

  def change_price(self, new_price):
    self.price = new_price

  def apply_discount(self, percentage):
    self.price = self.price - (self.price * (percentage / 100))