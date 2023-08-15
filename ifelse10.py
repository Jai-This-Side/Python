# Write a python program to find the eligibility of admission for a professional course
maths = int(input("enter marks obtained in maths\n"))
physics = int(input("enter marks obtained in physics\n"))
chemistry = int(input("enter marks obtained in chemistry\n"))

total = maths + physics + chemistry

if total >= 190 or maths+physics >= 140:
    print("candidate is eligible for the proffesional course")

else :
    print("candidate is not eligible for preffesional course")