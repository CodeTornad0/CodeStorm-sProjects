from random import sample

from cryptography.fernet import Fernet


def LoadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def View():
    x = input("Enter The Master Password: ")
    if x == masterPwd:
        try:
            with open("passwords.txt", "r") as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, passwd = data.split("|")
                    print(
                        f"User: {user} | Password: {fer.decrypt(passwd.encode()).decode()}"
                    )
        except Exception:
            print("No Passwords Found")
    else:
        print("Incorrect Master Password")


def Add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")


def Generate_Password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers = "1234567890"
    symbols = "!@#$%^&*()`~-=_+[]{}|;:,./<>?"
    characters = sample(lower + upper + numbers + symbols, 16)

    password = ""
    for character in characters:
        password += character
    print(f"Generated Password: {password}")


def Input():
    while True:
        try:
            mode = int(input("1. View 2. Add 3. Generate Password: "))
            if mode == 1:
                View()
            elif mode == 2:
                Add()
            elif mode == 3:
                Generate_Password()
            else:
                print("Invalid Action")
                Input()
        except Exception:
            print("Invalid Action")


key = LoadKey()
fer = Fernet(key)
masterPwd = input("Enter the master password: ")
Input()
