# class Backpack:
#     pass
# pass is a placeholder so that the class is not empty, 
# which would create an error alert.

from collections.abc import Sized


class House:
  def __init__(self, price, windows):
    self.price = price
    self.windows = windows

# self is a keyword that refers to the object that is calling the method.
# init is a method that is called when the object is created.
# a method is a function that is called when the object is called.

class Backpack:
  def __init__(self, color, size):
    self.items = []
    self.color = color
    self.size = size
# self has always to be the first parameter, 
# and it can be the only parameter if you don't want to use parameters.

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

class Movie:
  def __init__(self, title, year, language, rating):
    self.title = title
    self.year = year
    self.language = language
    self.rating = rating

# DEFAULT ARGUMENTS
class Circle:
  def __init__(self, radius=5):
    self.radius = radius
# 5 here is a default value, so if we omit the radius, 5 will be asign by default.
my_circle = Circle()
# since we are assnigning a default value, there won't be an Error Message above.
# the default arguments must be the LAST parameters in the list of parameters.

class Bacterium:
  def __init__(self, size, shape, multicel, metabolism, flagella_type, x, y):
    self.size = size
    self.shape = shape
    self.multicel = multicel
    self.metabolism = metabolism
    self.flagella_type = flagella_type
    self.x = x
    self.y = y

first_bac = Bacterium(0.5, "spherical", True, "heterotrophic", "monotrichous", 40, 35)

second_bac = Bacterium(0.8, "cylindrical", False, "autotrophic", "lophotrichous", 80, 65)

third_bac = Bacterium(0.6, "comma-shaped", False, "phothotrophic", "amphitrichous", 30, 55)
  
#Bacteria come in five basic shapes: spherical, cylindrical, comma-shaped, corkscrew and spiral.
# flagella = A-Monotrichous; B-Lophotrichous; C-Amphitrichous; D-Peritrichous

class Donut:
  def __ini__(self, flavor, toppings, filling, size):
    self.flavor = flavor
    self.toppings = toppings
    self.filling = filling
    self.size = size

class Customer:
  def __init__(self, name, age, address, favorite_dessert):
    self.name = name
    self.age = age
    self.address = address
    self.favorite_dessert = favorite_dessert

class Cake:
  def __init__(self, flavor, price, quality):
    self.flavor = flavor
    self.price = price
    self.quality = quality


# CLASS ATTRIBUTE

class Pizza:
  
  price = 12.99
  
  def __init__(self, description, toppings, crust):
    self.description = description
    self.toppings = toppings
    self.crust = crust

print(Pizza.price)

my_pizza = Pizza("Margherita", ["Basil", "Muschrooms"], "New York Style")
print(my_pizza.price)
Pizza.price = 13.99
print(Pizza.price)
print(my_pizza.price)





    