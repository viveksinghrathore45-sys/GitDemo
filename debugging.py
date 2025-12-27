# def display():
#     for i in range(1,11):
#         if i==10:
#            print("Bye")
# display()
#
# import random
#
# dice_numbers =["one","Two","Three","Four","Five","Six"]
# dice_num=random.randint(0,5)
# print(dice_numbers[dice_num])


number = int(input("Enter the number: "))
if number %3==0 and number %5==0:
        print("Fizzbuzz")
elif number%3==0:
        print("Fizz")
elif number %5==0:
        print("Buzz")
else:
        print(number)
