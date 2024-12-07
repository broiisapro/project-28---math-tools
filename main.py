import math

def main_menu():
    print("Welcome to the Math Tool App!\n")
    print("1. Calculate Area")
    print("2. Calculate Volume")
    print("3. Calculate Surface Area")
    print("4. Calculate Angles")
    print("5. Calculate Hypotenuse")
    print("6. Scientific Calculator")
    print("7. Other Tools")
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
    elif user_choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    print("\n--------------------------------------\n")
