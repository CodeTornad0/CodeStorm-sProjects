def Binary_Search(ascending_array, search_value):
    start = 0
    steps = 0
    end = len(ascending_array) - 1

    while start <= end:
        print(f"Step {steps}: {str(ascending_array[start:end+1])}")
        middle = (start + end) // 2
        if search_value == ascending_array[middle]:
            return middle
        if search_value < ascending_array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        steps += 1
    return print("Item not found")


array = input("Enter an array: ").split()
array.sort()
target = input("Enter a value to search: ")
Binary_Search(array, target)
