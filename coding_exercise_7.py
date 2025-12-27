height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

bmi= round(weight/height**2)
if bmi<18.5:
    print(f"Your BMI is {bmi} and you are under weight")
elif bmi<25:
    print(f"Your BMI is {bmi} and you are in normal weight")
elif bmi<30:
    print(f"Your BMI is {bmi} and you are overweight")
elif bmi<35:
    print(f"Your BMI is {bmi} and you are obese weight")
else:
    print(f"Your BMI is {bmi} and you are clinically obese weight")

