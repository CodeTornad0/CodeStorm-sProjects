import random
import pyautogui as pyauto

# this will minimize and maximize programs that are opened as well as clicking randomly
print("Keep The Amount Of Clicks Small")
clicks = input(
    "Clicks [There Is Always A Chance That It Will Click On Something You Don't Want Like It Clicking On Shutdown]: "
)
while clicks.isdigit() is False:
    print("Enter An Integer")
    clicks = input(
        "Clicks [There Is Always A Chance That It Will Click On Something You Don't Want Like It Clicking On Shutdown]: "
    )
for _ in range(int(clicks)):
    h = random.randint(0, 1080)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration=0.3)
    pyauto.hotkey("ctrl", "command", "f")
