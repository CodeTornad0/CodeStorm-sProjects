import webbrowser
from tkinter import *
from tkinter import ttk


def Search():
    webbrowser.open(website.get() + search.get())


def RunInTerminal():
    print(
        "Type In Your URL, But Make Sure To Type '/search?q=' At The End. This Can Very Based Off Of Your Website. For Example, You Have To Type '/results?search_query=' For YouTube. Make Sure You Check With The Website."
    )
    while True:
        website = input("Website: ")
        search = input("Search: ")
        webbrowser.open(website + search)


def RunInWindow():
    global website, search
    window = Tk()
    window.title("Search Engine")
    x = int(window.winfo_screenwidth() / 2 - 250)
    y = int(window.winfo_screenheight() / 2 - 250)
    window.geometry(f"500x500+{x}+{y}")
    google = StringVar(window, value="http://google.com/search?q=")
    python = StringVar(window, value="Python Is The Best Programming Language!!!!!")
    website = ttk.Entry(window, width=50, textvariable=google)
    search = ttk.Entry(window, width=50, textvariable=python)
    go = Button(window, text="Go", command=Search)
    website.place(x=250, y=250, anchor=CENTER)
    search.place(x=250, y=280, anchor=CENTER)
    go.place(x=250, y=310, anchor=CENTER)
    mainloop()


while True:
    userInput = input("Action 1. Run From Terminal 2. Run From Window: ")
    if userInput.isdigit():
        userInput = int(userInput)
        if userInput == 1:
            RunInTerminal()
        if userInput == 2:
            RunInWindow()
            break
        print("Invalid Input")
    else:
        print("Invalid Input")
website = ""
search = ""
