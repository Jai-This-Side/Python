# Write a python program to accept the height of a person in centimeter and categorize the person according to their height.
height = int(input("enter your height in centimeteres\n"))
if height<147:
    print("the person is dwarf")
if height<=176:
    print("the person has average height")
if height>176:
    print("the person is tall")