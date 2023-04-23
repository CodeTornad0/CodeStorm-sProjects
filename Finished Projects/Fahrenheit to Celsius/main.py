while True:
    temperature = input("Temperature: ")
    try:
        temperature = float(temperature)
        break
    except ValueError:
        print("Invalid Input")
convert = input("Convert To C˚ Or F˚: ").lower()
while convert not in ["c", "f"]:
    print("Invalid Input")
    convert = input("Convert To C˚ Or F˚: ")
if convert == "c":
    print(f"{temperature}˚ F is equal to {round((temperature - 32) * 5/9, 2)}˚ C")
else:
    print(f"{temperature}˚ C is equal to {round(temperature * 1.8 + 32, 2)}˚ F")
