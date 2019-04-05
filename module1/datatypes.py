students=[
    {"id":"sports","name":"vick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"action","name":"bick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"003","name":"vick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"004","name":"vick nick","age":32,"sex":"male","height":"167cm"},
    {"id":"005","name":"vick nick","age":32,"sex":"male","height":"167cm"}

]
def get_student_details (id,students):
    for student in students:
        if (student["id"]==id):
          return student
student_info = get_student_details ("sports",students)
print(student_info)

num = 1
while num < 101:
    if num % 15 == 0:
        print('fizzbuzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)
    num += 1  

kg = 1000
def convert_grammes_to_kilogrames (g):
    return str(g/kg) + "kg"
print (convert_grammes_to_kilogrames (5000)) 

def find_max_num (numbers):
    max_num  = 0
    for num in numbers:
        if num > max_num:
            max_num = num
            continue
    return max_num   

items = [1,2,3,4,5]
for item in items:
    item * 2
print(item)   