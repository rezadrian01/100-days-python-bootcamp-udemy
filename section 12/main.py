import random

print("Welcome to the number guessing Game!")
print("Im thinking of a number between 1 and 100")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

change = 0
if dificulty == 'easy':
    change = 10
elif dificulty == 'hard':
    change = 5
answer = random.randint(1, 100)

is_over = False

while change > 0 and not is_over:
    print(f"You have {change} attemps remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! the answer was {answer}")
        is_over = True
    else:
        change -= 1
        if guess < answer:
            print("Too low")
        else:
            print("Too high")
        print("Guess again")