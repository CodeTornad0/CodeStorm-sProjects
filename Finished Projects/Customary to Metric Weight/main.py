while True:
    try:
        weight = float(input("Weight: "))
        break
    except ValueError:
        print("Invalid Input")
unit = input("(K)g / (L)bs: ")
while unit.upper() not in ["K", "L"]:
    print("Invalid Input")
    unit = input("(K)g / (L)bs: ")
if unit.upper() == "K":
    converted = round(weight * 0.453592, 2)
    print(f"Weight In Kg: {converted}")
else:
    converted = round(weight / 0.453592, 2)
    print(f"Weight In Lbs: {converted}")
