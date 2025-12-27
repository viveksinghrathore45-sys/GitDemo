import random
import os

from colorama.ansi import clear_screen

import logo
import data_higherlower


score=0

def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess ==1:
            return True
        else:
            return False

account_2 = random.choice(data_higherlower.data)
continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(data_higherlower.data)
    while account_1 == account_2:
        account_2 = random.choice(data_higherlower.data)
    print(f"Compare 1: {display_accountinfo(account_1)}")
    print(logo.logo_1)
    print(f"Compare 2: {display_accountinfo(account_2)}")

    guess = int(input("Who has more followers ? Type 1 or 2: "))
    followers_count_1= account_1["follower_count"]
    followers_count_2= account_2["follower_count"]
    is_correct = check_answer(guess,followers_count_1,followers_count_2)
    os.system('cls')
    if is_correct:
     score += 1
     print(f"You are right . Your score is {score}")
    else:
     print(f"You are wrong .. Your Final score is {score}")
     continue_flag = False