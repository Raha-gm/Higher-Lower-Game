from art import logo, vs
from game_data import data
import random


# Format account information
def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name} | {account_description} | {account_country}"


# Check which account has more followers
def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count and guess == 'a':
        return True
    elif b_follower_count > a_follower_count and guess == 'b':
        return True
    else:
        return False


score = 0
should_continue_game = True

account_b = random.choice(data)

while should_continue_game:
    print(logo)

    # Choose a new account for A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    # Display account information
    print(f"A: {format_data(account_a)}")
    print(vs)
    print(f"B: {format_data(account_b)}")

    # Get the user's guess
    guess = input('Which account has more followers? Type A or B: ').lower()

    # Get follower counts
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    # Check the answer
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print('\n' * 2)

    # Give feedback and update the score
    if is_correct:
        score += 1
        print("You're right!")
        print(f"Current score: {score}")
    else:
        print("Sorry, that's wrong.")
        print(f"Final score: {score}")
        should_continue_game = False