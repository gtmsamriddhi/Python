Correct_num = 27
Max_attempts = 10
attempts = 0

while attempts < Max_attempts:
    try:
        my_guess = int(input("Enter your guess number: "))

        if my_guess == Correct_num:
            print("Congrats! You guessed it right!")
            break

        attempts += 1
        print(
            f"You guessed incorrectly. Attempts left: {Max_attempts - attempts}"
        )

    except ValueError:
        print("It works only for integer values. Try again.")

if attempts == Max_attempts and my_guess != Correct_num:
    print(f"You have 0 attempts left. You lost.\nCorrect answer = {Correct_num}")


Correct_num = 7
Max_attempts = 4
attempts = 0
found = False  # FLAG
while attempts < Max_attempts:
    try:
        my_guess = int(input("Enter your guess number: "))
        attempts += 1
        if my_guess == Correct_num:
            print("Congrats! You guessed it right!")
            found = True  # set flag
            break
        print(f"You guessed incorrectly. Attempts left: {Max_attempts - attempts}")

    except ValueError:
        print("It works only for integer values. Try again.")

if not found:
    print(f"You have 0 attempts left. You lost.\nCorrect answer = {Correct_num}")
