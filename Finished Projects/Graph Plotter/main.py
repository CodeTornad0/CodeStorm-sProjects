import matplotlib.pyplot as plt


def Handle_Input():
    while True:
        number_list = input("Enter a list of numbers: ").split()
        try:
            number_list = list(map(float, number_list))
            return number_list
        except ValueError:
            print("Invalid input. Numbers only allowed")


print("Put a space between each number")
while True:
    x = Handle_Input()
    y = Handle_Input()
    try:
        plt.plot(x, y)
        break
    except ValueError as error:
        print()
        print("Error:")
        print(error)
        print()

x_name = input("Enter the name of the x axis: ")
y_name = input("Enter the name of the y axis: ")
title = input("Enter the title of the graph: ")

plt.xlabel(x_name)
plt.ylabel(y_name)
plt.title(title)
plt.show()
