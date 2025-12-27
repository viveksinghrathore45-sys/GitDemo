student_data=[
    {
        "Name":"Vivek",
        "Age":21,
        "Roll_no":25,
        "Course":"Puthon"
    },
    {
        "Name":"Rahul",
        "Age":25,
        "Roll_no":24,
        "Course":"Java"
    }

]

def new_student_data(name,age,roolno,course_opted):
    new_student={}
    new_student["Name"]=name
    new_student["Age"]=age
    new_student["Roll_no"]=roolno
    new_student["Course"]=course_opted
    student_data.append(new_student)
new_student_data("Anurag",23,18,"C++")
print(student_data)

