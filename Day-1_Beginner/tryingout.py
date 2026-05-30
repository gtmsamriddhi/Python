name = input("Enter your name: ")
favcolor = input("Enter your fav color: ")
print (f"Oh wow!{name}\nyour choice of favcolor as {favcolor} is graet choice")
while True:
 try: 
  a = int(input("Enter first num: ")) # if not int it will result in 2+2 is 22
  b = int(input ("Enter second num to sum : "))
  sum = (a+b)
  print ("sum is : ", sum)
  break
 except ValueError:
  print("It works with only int values so try intger num")

age = int(input("Enter your age: "))
degree_input = input("Do you have a degree? (yes/no): ")
has_degree = degree_input.lower() == "yes"

if age >= 18 and has_degree:
    print("Eligible")
else:
    print("Not eligible")