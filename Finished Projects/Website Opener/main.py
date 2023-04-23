import webbrowser
import random
from time import sleep

websites = [
    "https://www.google.com/",
    "https://www.youtube.com/",
    "https://www.twitter.com/",
    "https://www.instagram.com/",
]
while True:
    webbrowser.open(random.choice(websites))
    sleep(random.randint(1, 5))
