import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    user_guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if user_guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
