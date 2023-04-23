from tkinter import Tk, StringVar
from tkinter.ttk import Button, OptionMenu
import time
import threading

clicks = 0


def Timer():
    time_left = options.get()
    time_left = int(time_left)
    time.sleep(time_left)
    print(f"CPS: {round(clicks/time_left, 2)}")
    click.place_forget()
    restart.place(relx=0.5, rely=0.55, anchor="center")


def Clicked():
    global clicks
    if options.get() != "":
        if clicks == 0:
            t = threading.Thread(target=Timer)
            t.start()
        clicks += 1
    else:
        print("Please Enter Your Time To Click")


def Restart():
    global clicks
    clicks = 0
    restart.place_forget()
    click.place(relx=0.5, rely=0.5, anchor="center")


window = Tk()
window.title("Clicking Speed Test")
window.geometry(f"500x500")
options = StringVar()
click_time = OptionMenu(window, options, 0, 1, 5, 10, 15, 30, 60)
click = Button(window, text="Click Here", command=Clicked)
restart = Button(window, text="Restart", command=Restart)
click_time.place(relx=0.5, rely=0.45, anchor="center")
click.place(relx=0.5, rely=0.5, anchor="center")
restart.place(relx=0.5, rely=0.55, anchor="center")
restart.place_forget()
window.mainloop()
