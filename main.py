from higher_lower_art import logo, vs
from higher_lower_game_data import data
from os import system
import random

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def compare(user_guess, follower_account_1, follower_account_2):
    if follower_account_1 > follower_account_2:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


account_2 = random.choice(data)
game_over = False
score = 0

print(logo)

while not game_over:
    account_1 = account_2
    account_2 = random.choice(data)

    if account_1 == account_2:
        account_2 = random.choice(data)


    print(f"Account A : {format_data(account_1)}")
    print(vs)
    print(f"Account B : {format_data(account_2)}")

    account_1_follower = account_1["follower_count"]
    account_2_follower = account_2["follower_count"]

    guess = input("Guess who has more follower ? Type 'A' for a or type 'B' for b : ").lower()

    system('cls')
    print(logo)

    compare(guess, account_1_follower, account_2_follower)

    compare_return = compare(guess, account_1_follower, account_2_follower)

    if compare_return == True:
        score += 1
        print(f"Your current score is {score}")
    else:
        print(f"Your current score is {score}")
        game_over = True



