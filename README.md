## Overview

This Math Tool App provides a collection of mathematical utilities to help users with various calculations. The app offers a range of functions, including basic arithmetic, geometry calculations, trigonometric operations, and a scientific calculator. It's designed to be interactive and user-friendly, allowing users to choose from different mathematical tools.

## Features

- **Calculate Area**: Calculates the area of various shapes such as squares, rectangles, circles, and triangles.
- **Calculate Volume**: Calculates the volume of 3D shapes such as cubes, rectangular prisms, spheres, cylinders, and cones.
- **Calculate Surface Area**: Calculates the surface area of 3D shapes like cubes, rectangular prisms, spheres, and cylinders.
- **Calculate Angles**: Computes sine, cosine, and tangent for a given angle in degrees.
- **Calculate Hypotenuse**: Computes the hypotenuse of a right triangle given the lengths of the other two sides using the Pythagorean theorem.
- **Scientific Calculator**: Allows users to input complex mathematical expressions, including trigonometric functions, and calculates the result.
- **Other Tools**: Includes additional tools like calculating factorials and logarithms with custom bases.

## Requirements

This app requires Python 3 and the `math` module (which is part of the Python standard library).

## Functions

### `main_menu()`
Displays the main menu with available options for the user to select a calculation.

### `calculate_area()`
Prompts the user to choose a shape (Square, Rectangle, Circle, Triangle) and calculates its area.

### `calculate_volume()`
Prompts the user to choose a 3D shape (Cube, Rectangular Prism, Sphere, Cylinder, Cone) and calculates its volume.

### `calculate_surface_area()`
Prompts the user to choose a 3D shape (Cube, Rectangular Prism, Sphere, Cylinder) and calculates its surface area.

### `calculate_angles()`
Prompts the user to choose a trigonometric function (Sine, Cosine, Tangent) and calculates the value for the given angle in degrees.

### `calculate_hypotenuse()`
Calculates the hypotenuse of a right triangle given the lengths of the other two sides.

### `scientific_calculator()`
Allows the user to input a mathematical expression (e.g., `2+2`, `sin(30)`) and evaluates it using Python's built-in math functions.

### `other_tools()`
Includes extra tools for calculating factorials and logarithms. The logarithm can be computed with a custom base.

## Usage

### Running the App
1. To start the app, run the script in Python.
2. The main menu will appear, allowing the user to select an option by entering the corresponding number (e.g., `1` to calculate the area).
3. Follow the prompts to enter necessary values (e.g., lengths, radii, angles).
4. Results will be displayed after the calculation.
5. To exit the app, select option `0` from the main menu.

## Notes

- This program runs in a loop, allowing users to perform multiple calculations without restarting.
- All input values are taken as floating-point numbers, except for the factorial tool, which accepts integers.
- The scientific calculator uses the `eval()` function to evaluate user input expressions safely by limiting access to Python's built-in functions, allowing only the functions from the `math` module.
