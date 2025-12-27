# class Humann:
#     def eat(self):
#         print("I can eat")
#
# class Male:
#     def flirt(self):
#         print("I can flirt")
#
# class Boy(Humann,Male):
#     pass
#
# boy_1=Boy()
# boy_1.eat()
# boy_1.flirt()


# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
#
# class Male:
#     def flirt(self):
#         print("I can flirt")
#     def work(self):
#         print("I can code")
#
# class Boy(Human, Male):
#     def sleep(self):
#         print("I can sleep")
#     def work(self):
#         print("I can Text")
#
# boy_1 = Boy()
# Human.work(boy_1)
# Male.work(boy_1)
# boy_1.work()

# class Human:
#     def __init__(self):
#         print("Calling init from Human ")
#         self.num_eyes=2
#         self.num_nose=1
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male:
#     def __init__(self,name):
#         print("Calling init from Male")
#         self.name =name
#     def flirt(self):
#         print("I can flirt")
#
#     def work(self):
#         print("I can Code")
#
# class Boy(Human,Male):
#     def __init__(self,name):
#         Human.__init__(self)
#         Male.__init__(self,name)
#     def sleep(self):
#         print("I can sleep")
#
#     def work(self):
#         print("I can Text")
# boy_1 = Boy("Vivek")
# print(boy_1.num_eyes)


