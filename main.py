import math
import numpy as np
import matplotlib.pyplot as plt

def main_menu():
    print("Welcome to the Math Tool App!\n")
    print("1. Calculate Area")
    print("2. Calculate Volume")
    print("3. Calculate Surface Area")
    print("4. Calculate Angles")
    print("5. Calculate Hypotenuse")
    print("6. Scientific Calculator")
    print("7. Other Tools")
    print("8. Matrix Operations")
    print("9. Prime Number Check")
    print("10. Solve Quadratic Equation")
    print("11. Unit Converter")
    print("12. Graphing Functions")
    print("0. Exit")

    choice = input("Select an option: ")
    return choice

# Utility functions for calculations
def calculate_area():
    print("\nChoose shape for area calculation:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    choice = input("Select a shape: ")

    if choice == "1":
        side = float(input("Enter the side length of the square: "))
        print(f"Area of square: {side ** 2}")
    elif choice == "2":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Area of rectangle: {length * width}")
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area of circle: {math.pi * radius ** 2}")
    elif choice == "4":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Area of triangle: {0.5 * base * height}")
    else:
        print("Invalid choice.")

def calculate_volume():
    print("\nChoose shape for volume calculation:")
    print("1. Cube")
    print("2. Rectangular Prism")
    print("3. Sphere")
    print("4. Cylinder")
    print("5. Cone")
    choice = input("Select a shape: ")

    if choice == "1":
        side = float(input("Enter the side length of the cube: "))
        print(f"Volume of cube: {side ** 3}")
    elif choice == "2":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        print(f"Volume of rectangular prism: {length * width * height}")
    elif choice == "3":
        radius = float(input("Enter the radius: "))
        print(f"Volume of sphere: {(4/3) * math.pi * radius ** 3}")
    elif choice == "4":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        print(f"Volume of cylinder: {math.pi * radius ** 2 * height}")
    elif choice == "5":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        print(f"Volume of cone: {(1/3) * math.pi * radius ** 2 * height}")
    else:
        print("Invalid choice.")

def calculate_surface_area():
    print("\nChoose shape for surface area calculation:")
    print("1. Cube")
    print("2. Rectangular Prism")
    print("3. Sphere")
    print("4. Cylinder")
    choice = input("Select a shape: ")

    if choice == "1":
        side = float(input("Enter the side length: "))
        print(f"Surface area of cube: {6 * side ** 2}")
    elif choice == "2":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        print(f"Surface area of rectangular prism: {2 * (length * width + width * height + height * length)}")
    elif choice == "3":
        radius = float(input("Enter the radius: "))
        print(f"Surface area of sphere: {4 * math.pi * radius ** 2}")
    elif choice == "4":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        print(f"Surface area of cylinder: {2 * math.pi * radius * (radius + height)}")
    else:
        print("Invalid choice.")

def calculate_angles():
    print("\nAngle Calculator:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    choice = input("Select a function: ")

    angle = float(input("Enter the angle in degrees: "))
    radians = math.radians(angle)

    if choice == "1":
        print(f"Sine({angle}): {math.sin(radians)}")
    elif choice == "2":
        print(f"Cosine({angle}): {math.cos(radians)}")
    elif choice == "3":
        print(f"Tangent({angle}): {math.tan(radians)}")
    else:
        print("Invalid choice.")

def calculate_hypotenuse():
    print("\nHypotenuse Calculator:")
    side_a = float(input("Enter side A: "))
    side_b = float(input("Enter side B: "))
    hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
    print(f"Hypotenuse: {hypotenuse}")

def scientific_calculator():
    print("\nScientific Calculator:")
    expression = input("Enter a mathematical expression (e.g., 2+2, sin(30)): ")
    try:
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

def other_tools():
    print("\nOther Tools:")
    print("1. Factorial")
    print("2. Logarithm")
    choice = input("Select a tool: ")

    if choice == "1":
        num = int(input("Enter a number: "))
        print(f"Factorial of {num}: {math.factorial(num)}")
    elif choice == "2":
        num = float(input("Enter a number: "))
        base = float(input("Enter the base (default is e): ") or math.e)
        print(f"Logarithm of {num} to base {base}: {math.log(num, base)}")
    else:
        print("Invalid choice.")

# Matrix Operations
def matrix_operations():
    print("\nMatrix Operations:")
    print("1. Matrix Addition")
    print("2. Matrix Multiplication")
    print("3. Determinant")
    print("4. Inverse Matrix")
    choice = input("Select an operation: ")

    if choice == "1" or choice == "2":
        rows = int(input("Enter number of rows for the matrices: "))
        cols = int(input("Enter number of columns for the matrices: "))
        print("Enter elements for the first matrix:")
        matrix1 = np.array([[float(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])
        print("Enter elements for the second matrix:")
        matrix2 = np.array([[float(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])

        if choice == "1":
            print(f"Result of matrix addition:\n{np.add(matrix1, matrix2)}")
        elif choice == "2":
            print(f"Result of matrix multiplication:\n{np.dot(matrix1, matrix2)}")

    elif choice == "3":
        rows = cols = int(input("Enter the size of the square matrix: "))
        matrix = np.array([[float(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])
        print(f"Determinant of the matrix: {np.linalg.det(matrix)}")
    
    elif choice == "4":
        rows = cols = int(input("Enter the size of the square matrix: "))
        matrix = np.array([[float(input(f"Enter element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)])
        if np.linalg.det(matrix) != 0:
            print(f"Inverse of the matrix:\n{np.linalg.inv(matrix)}")
        else:
            print("Matrix is singular and does not have an inverse.")
    else:
        print("Invalid choice.")

# Prime Number Check
def prime_check():
    num = int(input("Enter a number to check if it's prime: "))
    if num <= 1:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")

# Solve Quadratic Equation
def quadratic_solver():
    print("\nQuadratic Equation Solver (ax^2 + bx + c = 0):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Roots are real and different: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Root is real and the same: {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"Roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

# Unit Converter
def unit_converter():
    print("\nUnit Converter:")
    print("1. Distance (Meters to Kilometers)")
    print("2. Temperature (Celsius to Fahrenheit)")
    choice = input("Select a conversion: ")

    if choice == "1":
        meters = float(input("Enter distance in meters: "))
        print(f"{meters} meters is {meters / 1000} kilometers.")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {(celsius * 9/5) + 32}°F.")
    else:
        print("Invalid choice.")

# Graphing Functionality
def graph_functions():
    print("\nGraphing Functions:")
    func = input("Enter a mathematical function to graph (e.g., sin(x), cos(x)): ")
    x_vals = [x for x in range(-10, 11)]
    y_vals = [eval(func.replace('x', str(x))) for x in x_vals]
    
    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of {func}')
    plt.grid(True)
    plt.show()

# Main program loop
while True:
    user_choice = main_menu()

    if user_choice == "1":
        calculate_area()
    elif user_choice == "2":
        calculate_volume()
    elif user_choice == "3":
        calculate_surface_area()
    elif user_choice == "4":
        calculate_angles()
    elif user_choice == "5":
        calculate_hypotenuse()
    elif user_choice == "6":
        scientific_calculator()
    elif user_choice == "7":
        other_tools()
    elif user_choice == "8":
        matrix_operations()
    elif user_choice == "9":
        prime_check()
    elif user_choice == "10":
        quadratic_solver()
    elif user_choice == "11":
        unit_converter()
    elif user_choice == "12":
        graph_functions()
    elif user_choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    print("\n--------------------------------------\n")
