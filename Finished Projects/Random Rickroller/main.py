import webbrowser
from time import sleep
from random import uniform

rick_roll = "https://www.youtube.com/watch?v=p7YXXieghto"
while True:
    sleep(uniform(60 * 60, 60 * 60 * 3))
    webbrowser.open(rick_roll)
