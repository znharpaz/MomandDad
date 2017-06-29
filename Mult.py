def divide(g,h):
    print( g / h)

def subtract(g,h):
    print( g - h)
    
def add(g,h):
    print( g + h)

def multiply(g,h):
    print( g * h)

while True:

    a = input("Pick a number to multiply.") 
    b = input("Pick another number to multiply.")
    multiply(int(a), int(b))




    a = input("Pick a number to add.") 
    b = input("Pick another number to add.")
    add(int(a), int(b))


    a = input("Pick a number to subtract.") 
    b = input("Pick another number to subtract.")
    subtract(int(a), int(b))


    a = input("Pick a number to divide.") 
    b = input("Pick another number to divide.")
    divide (int(a), int(b))