items = input("Enter a list of items with a space between each item: ").split()
item = input("Enter an item: ")

if item in items:
    index = items.index(item)
    print(
        f"The first instance of {item} is at the index of {index}. {item} can be considered item number {index + 1}"
    )
else:
    print("Item not found")
