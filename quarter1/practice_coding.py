class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = float(price)
  def product_details(self):
    print(f"Product Details:\nProduct Name: {self.name}\nPrice: {self.price}")

Products = [ ]

for i in range(5):
  name = input("Enter product name: ")
  price = float(input("Enter price of product: "))
  name = Product(name, price)
  Products.append(name)

print(Products)
