# Write a python program to read the value of an integer m and display the value of n is 1 when m is larger than 0, print n=0 when m is 0 and -1 when m is less than 0.
m = int(input("enter the number"))
if m>0:
    print("n is 1")
if m==0:
    print("n is 0")
if m<0:
    print("n is -1")