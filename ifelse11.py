# Write a python program to read roll no and marks of three subjects and calculate the total, percentage and division. 
roll_no = int(input("enter your roll number\n"))
physics = int(input("enter your marks in physics\n"))
chemistry = int(input("enter your marks in chemistry\n"))
it = int(input("enter your marks in IT\n"))

total = physics + chemistry + it

print("total marks obtained in all three subjects are",total)

percentage = total/300*100

print("percentage in all three subject is",percentage,"%")

if percentage < 60:
    print("you comes in third division")

if 80 > percentage > 60:
    print("you comes in second division")
    
if percentage > 80:
    print("you comes in first division")


