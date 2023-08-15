import formula
print("\t\t1 for cylinder")
print("\t\t2 for cone")
print("\t\t3 for sphere")
print("\t\t4 for rectangle")
print("\t\t5 for square\n")

pie = 3.14

choice_1 = int(input("\t\tEnter shape of your choice :\t"))

if choice_1 == 1:
    print("\n")
    print("\t\t1 for volume of cylinder")
    print("\t\t2 for total surface area of cylinder")
    print("\t\t3 for curved surface area of cylinder")

    print("\n")

    OperationCylinder = int(input("\t\tChoose operation you want to perform :\t"))

    if OperationCylinder == 1:
        radius = float(input("\t\tEnter the radius of the cylinder :\t"))
        height = float(input("\t\tenter the height of the cylinder\t"))
        result=formula.VolumeOfCylinder(radius,height)
        print("The volume of cylinder is",result)

    if OperationCylinder == 2:
        radius = float(input("\t\tEnter the radius of the cylinder :\t"))
        height = float(input("\t\tenter the height of the cylinder\t"))
        result=formula.TsaOfCylinder(radius,height)
        print("The TSA of cylinder is",result)

    if OperationCylinder == 3:
        radius = float(input("\t\tEnter the radius of the cylinder :\t"))
        height = float(input("\t\tenter the height of the cylinder\t"))
        result=formula.CsaOfCylinder(radius,height)
        print("The CSA of cylinder is",result)

if choice_1 == 2:

    print("\n")

    print("\t\t1 for volume of cone")
    print("\t\t2 for total surface area of cone")
    print("\t\t3 for curved surface area of cone")

    print("\n")

    OperationCone = int(input("\t\tChoose operation you want to perform :\t"))

    if OperationCone == 1:
        radius = float(input("\t\tEnter the radius of the cone :\t"))
        result = formula.VolumOfCone(radius)
        print("The volume of Cone is",result)

    if OperationCone == 2:
        radius = float(input("\t\tEnter the radius of the cone :\t"))
        SlantHeight = float(input("\t\tEnter the slant height of cone :\t"))
        result = formula.TsaOfCone(radius, SlantHeight)
        print("The TSA of Cone is",result)

    if OperationCone == 3:
        radius = float(input("\t\tEnter the radius of the cone :\t"))
        SlantHeight = float(input("\t\tEnter the slant height of cone :\t"))
        result = formula.CsaOfCone(radius, SlantHeight)
        print("The CSA of Cone is",result)

if choice_1 == 3:
    
    print("\n")

    print("\t\t1 for surface area of sphere")
    print("\t\t2 for volume of sphere")

    OperationSphere = int(input("Enter operation you want to perform :\t"))

    if OperationSphere == 1:
        radius = float(input("\t\tEnter the radius of sphere :\t"))
        result = formula.SurfaceAreaSphere(radius)
        print("The surface area of sphere is",result)

    if OperationSphere == 2:
        radius = float(input("\t\tEnter the radius of sphere :\t"))
        result = formula.VolumeOfSphere(radius)
        print("The volume of sphere is",result)

if choice_1 == 4:

    print("\n")

    print("\t\t1 for perimeter of rectangle")
    print("\t\t2 for area of rectangle")

    OperationRectangle = int(input("Enter operation you want to perform :\t"))

    if OperationRectangle ==1:
        length = int(input("Enter the length of rectangle"))
        breadth = int(input("Enter the breadth of rectangle"))
        result = formula.PerimeterOfRectangle(length, breadth)
        print("The perimeter of rectangle is",result)

    if OperationRectangle == 2:
        length = int(input("Enter the length of rectangle"))
        breadth = int(input("Enter the breadth of rectangle"))
        result = formula.AreaOfRectangle(length, breadth)
        print("The area of rectangle is",result)

if choice_1 == 5:

    print("\n")

    print("\t\t1 for perimeter of area")
    print("\t\t2 for area of area")

    OperationSquare = int(input("Enter operation you want to perform :\t"))

    if OperationSquare == 1:
        side = int(input("enter the side of square"))
        result = formula.PerimeterOfSquare(side)
        print("The perimeter of square is", result)

    if OperationSquare == 2:
        side = int(input("enter the side of square"))
        result = formula.AreaOfSquare(side)
        print("The area of square is", result)


