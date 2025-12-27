# class Human:
#     def eat(self):
#         print("I can eat")
#
# class Male(Human):
#     def sleep(self):
#         print("I can sleep")
#
# class Female(Human):
#     def work(self):
#         print("I can Code")
#
#     def sleep(self):
#         print("I can sleep")
#
# female_1=Female()
# female_1.eat()
# female_1.work()
# female_1.sleep()
# male_1=Male()
# male_1.eat()

# class Human:
#     def __init__(self,name):
#         self.num_eyes=2
#         self.num_nose=1
#         self.num_heart=1
#         self.name=name
#     def eat(self):
#         print("I can eat")
#
#
# class Male(Human):
#     def sleep(self):
#         print("I can sleep")
#
# class Female(Human):
#     def __init__(self,heart,name,num_eyes,num_nose):
#         self.name=name
#         self.num_eyes=num_eyes
#         self.num_nose=num_nose
#         self.heart=heart
#     def work(self):
#         print("I can work")
#     def display(self):
#         print(f"I am {self.name} and I have {self.heart} heart and {self.num_eyes} eyes and {self.num_nose} nose")
#
#
# female_1=Female(1,"Vivek",2,1)
# female_1.display()
