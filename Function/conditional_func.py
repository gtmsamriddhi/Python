def is_even(num):
    return num%2 == 0
print (is_even(8))
print (is_even(5))    

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(5))
print(check_number(-3))
print(check_number(0))

def larger(a, b):
    if a > b:
        return a
    else:
        return b
print(larger(10, 7))

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    else:
        return "D"
print(grade(85))

def admission(age, score):
    if age >= 18:
        if score >= 80:
            return "Accepted"
        else:
            return "Score too low"
    else:
        return "Too young"
print(admission(20, 85))
print(admission(20, 70))
print(admission(16, 90))

def find_largest(numbers):
    return max(numbers)

nums = [5, 12, 3, 8, 20, 1, 15, 7, 10, 4]
print(find_largest(nums))