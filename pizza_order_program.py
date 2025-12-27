size = (input("What size of pizza you want (S/M/L): "))
bill=0
if size == 'S' or size == 's':
    bill+=100
    print("Small Pizza Prize is 100RRs")
elif size == 'M' or size == 'm':
    bill+=200
    print("Medium Pizza Prize is 200RRs")
else :
    bill+=300
    print("Large Pizza Prize is 300RRs")

add_pepporoni = input("Do you want pepporoni? (Y/N) ")
if add_pepporoni == "Y" or add_pepporoni == "y":
    if size == 'S' or size == 's':
        bill = bill +30
    else:
        bill = bill +50
extra_cheese = input("Do you want extra  cheese? (Y/N) ")
if extra_cheese == "Y" or extra_cheese == "y":
    bill+=20

print(f"Your total bill is {bill}")
