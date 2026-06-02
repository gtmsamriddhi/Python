print ("Example for i in range 5")
for i in range(5):      
    print(i)
print ("Example for i in range 1 to 6")
for i in range(1, 6):   
    print(i)
print ("Example for i in range 0-10-2")
for i in range(0, 10, 2): # runs from 0 to 10 but 10 aint included and takes step size of 2- increses step by 2
    print(i)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
 print(fruit)
for idx, fruit in enumerate (fruits , 1):
   print (f" {idx}: {fruit}")

