import os
import webbrowser
from time import sleep

from gtts import gTTS
from playsound import playsound

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
rick_roll = "https://www.youtube.com/watch?v=p7YXXieghto"
bobux = input("Bobux Amount: ")
while bobux.isdigit() is False:
    print("Enter An Integer")
    bobux = input("Bobux Amount: ")
del bobux
account_name = input("Account Name: ")
account_id = input("Account ID: ")
account_password = input("Account Password: ")
print("Generating...")
text = f"I have your password dork. Account name {account_name}. Account I D {account_id}. Account password {account_password}."
output = gTTS(
    text=text,
    lang="en",
    slow=False,
)
output.save(f"{FILE_PATH}/loser.mp3")
sleep(5)
playsound(f"{FILE_PATH}/loser.mp3")
for _ in range(3):
    webbrowser.open(rick_roll)
