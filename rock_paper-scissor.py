import random

user_choice = int(input("Enter your choice: Type 0 for Rock , 1 For Paper , 2 OFr Scissor : "))
if user_choice >=3 or user_choice<0:
    print("You Enttered a invalid number , you lose")
else:
    computer_choice = random.randint(0,2)
    print(f"Computer Chose:{computer_choice}")
    if computer_choice == user_choice:
        print("its a draw")
    elif computer_choice ==0 and user_choice==2:
        print("You lose")
    elif user_choice ==0 and computer_choice==2:
        print("You Win")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice>computer_choice:
        print("you win")