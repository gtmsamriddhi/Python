for i in range(3):
    for j in range(2):
        print(i, j)

# i runs 0 1 2 and j runs 0 1  so combinations become 0 to 0 0, 0 1, 1 0 , 1 1  and 2 0 , 2 1 
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()
#*****
#*****
#*****