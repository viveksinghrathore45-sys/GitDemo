height= int(input("what is your height? "))

if height>=3:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    if age<12:
        print("Please pay 150Rs")
    elif age<=18:
        print("Please pay 250Rs")
    else:
        print("Please pay 500Rs")
else:
    print("Sorry you can not ride the roller coaster")
print("Bye")
