import pyautogui

pyautogui.PAUSE = 0

while True:
    try:
        wait = float(input("How Long Do You Want To Wait For Each Click: "))
        break
    except ValueError:
        print("Enter A Number")
while True:
    times = input("How Many Times Do You Want To Click [Enter Nothing For ∞]: ")
    if times.strip() == "":
        break
    try:
        times = int(times)
        break
    except ValueError:
        print("Enter An Integer")
block = input("Press Enter To Start")
if str(times).strip() != "":
    pyautogui.click(clicks=times, interval=wait)
else:
    while True:
        pyautogui.click(interval=wait)
