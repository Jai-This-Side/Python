pie = 3.14

def VolumeOfCylinder(radius, height):
    return pie*radius**2*height
    
def TsaOfCylinder(radius, height):
    return 2*pie*radius*(radius+height)

def CsaOfCylinder(radius, height):
    return 2*pie*radius*height

def VolumOfCone(radius):
    return 1/3*pie*radius**2

def CsaOfCone(radius,SlantHeight):
    return pie*radius*SlantHeight

def TsaOfCone(radius, SlantHeight):
    return pie*radius*(SlantHeight+radius)

def VolumeOfSphere(radius):
    return 4/3*pie*radius**3

def SurfaceAreaSphere(radius):
    return 4*pie*radius**2

def PerimeterOfRectangle(length, breadth):
    return 2*(length+breadth)

def AreaOfRectangle(lenght,breadth):
    return length*breadth

def PerimeterOfSquare(side):
    return 4*side

def AreaOfSquare(side):
    return side**2