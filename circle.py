"""
Calculate the area and circumference of a circle from its radius.
Steps:
    1. Prompt the user to enter a radius
    2. Covert the string value to an integer value
    3. Calculate the circumference
    4. Calculate the area
    5. Format and print the result
"""

import math

radius = int(input('Enter the radius of your circle:'))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'The circumference is {circumference}, the area is {area} '
      f'for the radius {radius}')