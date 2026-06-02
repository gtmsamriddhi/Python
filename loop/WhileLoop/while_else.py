MAX_ATTEMPTS = 5
CORRECT_PASSWORD = "secret"

attempts = 0

while attempts < MAX_ATTEMPTS:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Access granted!")
        break

    attempts += 1
    print(f"Incorrect password. Attempts remaining: {MAX_ATTEMPTS - attempts}")

if attempts == MAX_ATTEMPTS:
    print("Too many attempts. Access denied.")