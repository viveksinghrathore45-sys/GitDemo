height= int(input("What is your height? "))
if height>=3:
    print("you can ride the roller coaster")
    age = int(input("What is your age? "))
    if age<=18:
        print("please pay 250Rs")
    else:
        print("please pay 500Rs")

else:
    print("Sorry you can not ride the roller coaster")

print("bye")