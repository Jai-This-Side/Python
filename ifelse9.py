'''Write a python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point 
lies. '''
x_axis = int(input("enter the x coordinate\n"))
y_axis = int(input("enter the y coordinate\n"))

if x_axis > 0 and y_axis > 0 :
    print("the coordinate lies in first quadrant")

if x_axis < 0 and y_axis > 0 :
    print("the coordinate lies in second quadrant")

if x_axis < 0 and y_axis < 0 :
    print("the coordinate lies in third quadrant")

if x_axis > 0 and y_axis < 0 :
    print("the coordinate lies in fourth quadrant")