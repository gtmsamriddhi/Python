def greet(name):
    return "Hello, " + name
print(greet("Alice")) 

def greet(name, msg="Good morning"):
    return f"{msg}, {name}!"
print(greet("Bob"))           # Good morning, Bob!
print(greet("Bob", "Hi"))     # Hi bob

def add(a, b):
    return a + b

result = add(3, 5)
print(result)
print(result * 2)
print(result + 10)

