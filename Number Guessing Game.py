import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 50.")

    number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} tries.")
            break

if __name__ == "__main__":
    guess_number()
