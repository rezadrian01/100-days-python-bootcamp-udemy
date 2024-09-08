import random
from game_data import data
from art import logo, vs

def answer_check(user_answer, person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return user_answer == 'A'
    else:
        return user_answer == 'B'

def format_print(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"


def game():
    is_over = False
    total_score = 0
    person1 = random.choice(data)

    while not is_over:
        person2 = random.choice(data)
        while person1 == person2:
            person2 = random.choice(data)

        print(logo)
        if total_score > 0:
            print(f"You're right! Current score: {total_score}")
        print(f"Compare A: {format_print(person1)}")
        print(vs)
        print(f"Against B: {format_print(person2)}")
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_correct = answer_check(user_answer, person1, person2)
        if is_correct:
            person1 = person2
            total_score += 1
            print("\n" *20)
        else:
            is_over = True
            print("\n================Game Over=======================\n")
            print(f"Sorry that's wrong. Final score: {total_score}")


game()