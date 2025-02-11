""" This program calculates the area of a triangle. """
import math

# Request the lengths of all three sides of a triangle from the user
tri1 = float(input
             ("Provide the length of the first side in cm: "))
tri2 = float(input
             ("Provide the length of the second side in cm: "))
tri3 = float(input
             ("Provide the length of the third side in cm: "))
# Calculate the area
tri_s = float((tri1+tri2+tri3)/2.)
tri_a = float(math.sqrt(tri_s*(tri_s-tri1)*(tri_s-tri2)*(tri_s-tri3)))
print(str(f"The area of the triangle is {round(tri_a, 2)} cm2"))
