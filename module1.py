students=[
    {"id":"001","name":"vick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"002","name":"bick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"003","name":"vick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"004","name":"vick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"005","name":"vick nick","age":32,"sex":"male","height":"167cm"}

]
def get_student_details (id,students):
    for student in students:
        if (student["id"]==id):
          return student
student_info = get_student_details ("002",students)
print(student_info)
