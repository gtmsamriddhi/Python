print ("I am aspiring data engineer")
name = (input("Enter your name: "))

print("Hello", name)
age = int (input("enter your age: "))
if age >= 18:
 print ("you're an adult, you'll be:", age+1, "next your.")
else :
 print ("you're a minor")
x = 42
y = "hello"
z = 3.14
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(z)) 
age_text = "25" # this is a string
age_num = int(age_text) # convert to int
print(age_num + 1) # 26
price = 99
print(float(price)) # 99.0
num = 7
print(str(num)+ str(7))