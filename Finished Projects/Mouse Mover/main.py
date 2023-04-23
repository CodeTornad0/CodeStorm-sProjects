import pyautogui as pag
import random
import time

wait_time = input("Wait Time: ")
while wait_time.isnumeric is False:
    print("Only Integers Allowed")
    wait_time = input("Wait Time: ")
smoothness = input("Smoothness: ")
while smoothness.isdigit() is False:
    print("Only Integers Allowed")
    smoothness = input("Smoothness: ")
wait_time, smoothness = int(wait_time), int(smoothness)
while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, smoothness)
    time.sleep(wait_time)
