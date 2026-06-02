student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
for key in student:
    print(key)

for val in student.values():
    print(val)

for key, value in student.items():
    print(key, ":", value)