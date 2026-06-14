def greet(name):
    return "Hello, " + name
print(greet("Alice")) 

def greet(name, msg="Good morning"):
    return f"{msg}, {name}!"
print(greet("Bob"))           # Good morning, Bob!
print(greet("Bob", "Hi"))     # Hi bob

def happy_birthday(name):
    print (f"happy birthday {name}")
    print ("you are old now")
happy_birthday("sarthak")
happy_birthday("samriddhi")

def add(a, b):
    return a + b
print (add(3,5))
result = add(3, 5)
print(result)
print(result * 2)
print(result + 10)

def sub(a, b):
    print (f"Sub from b to a is :   {b-a}")
sub(5,8)

def square(a):
    return a * a
print(square(4))

def add(a,b):
    return a+b
result=add(2,3)
print(result)
print(result*2)

def multiply(a):
    return 5*a
result = multiply(4)
print (result)

def tax(price):
    return price*0.15
tax_amt=tax(200)
print(tax_amt)
total = 200 + tax_amt
print(total)

