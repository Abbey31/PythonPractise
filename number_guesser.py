import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess!= random_number:
        guess = input(f"Guess a number between ! and {x}")
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("sorry, guess again. Too high")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        guess = random.randint(low, high)
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")

computer_guess(10)

guess(10)