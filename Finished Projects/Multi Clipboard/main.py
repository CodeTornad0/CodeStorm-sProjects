import sys, clipboard, json
import os


FILE_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = FILE_PATH.split("CodeStorm-sProjects")[0]


savedData = f"{FILE_PATH}clipboard.json"


def saveData(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def loadData(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadData(savedData)
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        saveData(savedData, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
