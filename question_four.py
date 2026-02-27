# section C Questions

# qusetion 4(i)

# Object _oriented Programming is a programming paradym that deals with classes and objects

# Why OOP is important in Software
# Resuability: oop enables using of the same code
# it allows use of attributes and behaviours together in one code initiated
# it makes code readable and easy to understand


# question 4(iii)

def num( x, y):
    product = x * y
    return product
print (num(6,7))


# question 4(iv)

class Laptop():
    def __init__(self , brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


# Creating the  object
laptop1 = Laptop( "Lenovo", "itel" ,300000)


# print  attributes
print("Brand:", laptop1.brand)
print("Model:", laptop1.model)
print("Price:", laptop1.price)


# question 4(v)
class Laptop():
    def display(self):
        msg = "display_specs"
        return msg
    laptop1 = Laptop("Lenovo", "itel", 300000)
print(laptop1)

