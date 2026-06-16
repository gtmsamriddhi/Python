questions = [
    ("Capital of Nepal?", "B"),
    ("5 + 3 = ?", "B")
]

options = [
    ["A. Pokhara", "B. Kathmandu", "C. Delhi", "D. Tokyo"],
    ["A. 5", "B. 8", "C. 10", "D. 12"]
]

score = 0

for i in range(len(questions)):
    print("\nQ:", questions[i][0])

    for opt in options[i]:
        print(opt)

    answer = input("Your answer: ").upper()

    if answer == questions[i][1]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Final Score:", score)