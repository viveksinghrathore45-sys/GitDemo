height= int(input("What is your height? "))
bill =0
if height>=3:
    print("You can ride")
    age=int(input("What is your age?"))
    if age<12:
        bill=150
        print("Ticket price is 150Rs")
    elif age<=18:
        bill = 250
        print("Ticket price is 250Rs")
    else:
        bill = 500
        print("Ticket price is 500Rs")
    want_photo = input("Do you want photo? (Y/N) ")
    if want_photo == "y" or want_photo == "Y":
             bill = bill +50
    print(f"Your total bill is {bill}")

else:
    print("You cant ride")

print("Thank you ...... ekjoy the ride")