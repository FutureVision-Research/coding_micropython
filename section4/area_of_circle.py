# This script calculates the area of a circle and demonstrates how to use the math module

import math # Provides additional math abilities

# Ask the user for the radius in meters
radius = float(input("Enter the radius of the circle (in meters): "))

# Calculate the area using A = π * r²
area = math.pi * (radius ** 2)

# Display the result in square meters
print(f"The area of the circle is {area:.2f} square meters (m²).")
