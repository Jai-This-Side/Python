# Write a python program to find the largest of three numbers. 
num1 = int(input("enter the first number\n"))
num2 = int(input("enter the second number\n"))
num3 = int(input("enter the third number\n"))

if num1>num2 and num1>num3 :
    print("first number is greates among all")

if num2>num1 and num2>num3 :
    print("second number is greatest among all")

if num3>num1 and num3>num2 :
    print("third number is greatest among all")