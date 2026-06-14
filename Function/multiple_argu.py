def add_all(*args):
    return sum(args)
add_all(1, 2, 3, 4) 

def find_highest(*args):
    print(f"given numbers : {(args)}" )      
    return max(args)   
print(f"highest num is : {(find_highest(3, 7, 1, 9, 2))}")

def find_average(*args):
    print(f"given numbers : {(args)}" )     
    return sum(args) / len(args)
print(f"average is : {(find_average(3, 7, 1, 9, 2))}")

def find_all(*args):
    print(f"numbers are: {args}")
    print("Highest:", max(args))
    print("Lowest: ", min(args))
    print("Average:", sum(args) / len(args))

find_all(3, 7, 1, 9, 2)