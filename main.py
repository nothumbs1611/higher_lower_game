# import logo and data

from art import logo
from art import vs
from game_data import data
import random

# select player
def player():
    return random.choice(data)

# format the data into printable format: name, description, country
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print it out:
    print(f"{name}, a {description}, from {country}")
# check number of followers against user's guess and return True if they got it right, or false if they got it wrong
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
# build game
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = player()
    account_b = player()

    while game_should_continue:
        
        account_a = account_b
        account_b = player()
        
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b )}.")
    
        guess = input("Who has more followers on social media? Type 'A' or 'B' ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
        print("\033[H\033[J")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score is {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong.  Final score is: {score}")
game()
    
