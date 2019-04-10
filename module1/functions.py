#Write a program that asks the user how many Fibonnaci 
# numbers to generate and then generates them.
nterms = int(input("how many terms?"))
#first two terms
n1 = 0
n2 = 1
count = 0
#check if the number of terms is valid
if nterms <=0:
	print("please enter a positive integer")
elif nterms ==1:
	print("fibonacci sequence upto", nterms,":")
	print(n1)
else:
	print("fibonacci sequence upto",nterms,":")
	while count <nterms:
		print (n1, end=',')
		nth = n1 + n2
		#update values
		n1 =n2
		n2 = nth
		count += 1


#Write a function that returns student information if given a
#  “student id” and a list of students as a parameter. 
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