import math


def Create_Rectangle(width, height):
    for _ in range(height):
        for _ in range(width):
            print("*", end="")
        print()


def Create_Triangle(width):
    for i in range(1, width + 1):
        for _ in range(i):
            print("*", end="")
        print()


def Create_Diamond(width):
    for i in range(1, (width + 1) // 2 + 1):
        for _ in range(width // 2 - i + 1):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print("*", end="")
        print()
    for i in range((width + 1) // 2 + 1, width + 1):
        for _ in range(i - width // 2 - 1):
            print(" ", end="")
        for _ in range(2 * (width - i + 1) - 1):
            print("*", end="")
        print()


def Create_Circle(radius):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if math.sqrt(x**2 + y**2) <= radius:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def Check_Number(number, name):
    while number.isdigit() is False or int(number) < 1:
        print("Enter an integer greater than 0")
        number = input(f"Enter the {name}: ")
    return int(number)


functions = {
    "1": Create_Rectangle,
    "2": Create_Triangle,
    "3": Create_Diamond,
    "4": Create_Circle,
}
shape_type = input(
    "Enter the shape type (1. rectangle, 2. triangle, 3. diamond, 4. circle): "
)
while shape_type not in functions:
    print("Invalid shape type")
    shape_type = input(
        "Enter the shape type (1. rectangle, 2. triangle, 3. diamond, 4. circle): "
    )
function = functions.get(shape_type)
if shape_type != "4":
    width = input("Enter the width: ")
    width = Check_Number(width, "width")
    if shape_type != "1":
        function(width)
if shape_type == "1":
    height = input("Enter the height: ")
    height = Check_Number(height, "height")
    function(width, height)
if shape_type == "4":
    radius = input("Enter the radius: ")
    radius = Check_Number(radius, "radius")
    function(radius)
