import random

names = input("Enter everybody`s  neme seperatsd by commas: ")
names_list = names.split(",")
lenght = len(names_list)
random_choice = random.randint(0,lenght-1)
print(f"{names_list[random_choice]} Will pay the bill")