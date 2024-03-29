import math

# Define the parent class 3D Shapes
class Shapes3D:
    # Define the constructor with attributes radius and height
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # Define the method print Volume
    def print_Volume(self):
        # Calculate the volume using the formula for each shape
        if isinstance(self, Cylinder):
            volume = math.pi * self.radius ** 2 * self.height
        elif isinstance(self, Sphere):
            volume = 4 / 3 * math.pi * self.radius ** 3
        else:
            volume = 0

        # Print the volume with two decimal places
        print("The volume of the {} is {:.2f}".format(self.__class__.__name__, volume))

    # Define the method print Area
    def print_Area(self):
        # Calculate the area using the formula for each shape
        if isinstance(self, Cylinder):
            area = 2 * math.pi * self.radius * (self.radius + self.height)
        elif isinstance(self, Sphere):
            area = 4 * math.pi * self.radius ** 2
        else:
            area = 0

        # Print the area with two decimal places
        print("The area of the {} is {:.2f}".format(self.__class__.__name__, area))

# Define the child class Cylinder by inheriting 3D Shapes class
class Cylinder(Shapes3D):
    # Use the parent constructor with radius and height as parameters
    def __init__(self, radius, height):
        super().__init__(radius, height)

# Define the child class Sphere by inheriting 3D Shapes class
class Sphere(Shapes3D):
    # Use the parent constructor with radius as parameter and height as zero
    def __init__(self, radius):
        super().__init__(radius, 0)

# Get the user input for radius and height of cylinder
try:
    cylinder_radius = float(input("Enter the radius of cylinder: "))
    cylinder_height = float(input("Enter the height of cylinder: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    # Create an object of Cylinder class with user input values
    cylinder = Cylinder(cylinder_radius, cylinder_height)
    # Call the print Volume and print Area methods for cylinder object
    cylinder.print_Volume()
    cylinder.print_Area()

# Get the user input for radius of sphere
try:
    sphere_radius = float(input("Enter the radius of sphere: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    # Create an object of Sphere class with user input value
    sphere = Sphere(sphere_radius)
    # Call the print Volume and print Area methods for sphere object
    sphere.print_Volume()
    sphere.print_Area()