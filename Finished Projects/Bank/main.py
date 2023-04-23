class Account:
    def __init__(self, balance):
        self.balance = balance


def Create_Account():
    name = input("Enter The Name Of The Account: ")
    if name in account_info:
        print("This Account Already Exist")
        return
    if len(name) < 3:
        print("Please Enter A Longer Name")
        return
    try:
        balance = float(input("Enter The Amount Of Money Inside: "))
    except ValueError:
        print("Please Enter A Number")
        return
    if round(float(balance), 2) < 0:
        print("Please Enter A Valid Number Greater Than Or Equal To Zero")
        return
    globals()[name] = Account(balance)
    account_info[name] = round(float(balance), 2)


def Check_Status():
    name = input(
        "Enter The Name Of The Account You Would Like To See [Enter Nothing For All]: "
    )
    if not account_info:
        print("Your Record Is Empty")
        return
    if name.strip() == "":
        return print(account_info)
    if name in account_info:
        return print(float(account_info[name]))
    return print("This Account Doesn't Exist")


def Deposit():
    desired_account = input(
        "Enter The Name Of The Account You Would Like To Deposit Money To: "
    )
    if desired_account not in account_info:
        print("This Account Doesn't Exist")
        return
    try:
        amount = float(input("Enter The Amount Of Money You Would Like To Add: "))
    except ValueError:
        print("Please Enter A Number")
        return
    if round(float(amount), 2) < 0:
        print("Please Enter A Number Greater Than Or Equal To Zero")
        return
    globals()[desired_account].balance = round(
        globals()[desired_account].balance + float(amount), 2
    )
    account_info[desired_account] = globals()[desired_account].balance


def Transfer():
    desired_account = input(
        "Enter The Name Of The Account You Would Like To Add Money To: "
    )
    supplier_account = input(
        "Enter The Name Of The Account You Will Be Taking Money From: "
    )
    if desired_account not in account_info or supplier_account not in account_info:
        print("This Account Doesn't Exist")
        return
    try:
        amount = float(
            input(f"Enter How Much Money You Would Like To Add To {desired_account}: ")
        )
    except ValueError:
        print("Please Enter A Number")
        return
    if round(amount, 2) < 0:
        print("Please Enter A Number Greater Than Or Equal To Zero")
        return
    if float(globals()[supplier_account].balance) - round(float(amount), 2) < 0:
        print("You Don't Have The Required Money To Complete The Transaction")
        return
    globals()[desired_account].balance = round(
        float(globals()[desired_account].balance) + float(amount), 2
    )
    globals()[supplier_account].balance = round(
        float(globals()[supplier_account].balance) - float(amount), 2
    )
    account_info[desired_account], account_info[supplier_account] = (
        globals()[desired_account].balance,
        globals()[supplier_account].balance,
    )


def Withdraw():
    desired_account = input(
        "Enter The Name Of The Account You Would Like To Withdraw Money From: "
    )
    if desired_account not in account_info:
        print("This Account Doesn't Exist")
        return
    try:
        amount = float(input("Enter The Amount Of Money You Would Like To Take Out: "))
    except ValueError:
        print("Please Enter A Number")
        return
    if round(float(amount), 2) < 0:
        print("Please Enter A Number Greater Than Or Equal To Zero")
        return
    if float(globals()[desired_account].balance) - round(float(amount), 2) < 0:
        print("You Don't Have The Required Money To Complete The Transaction")
        return
    globals()[desired_account].balance = round(
        float(globals()[desired_account].balance) - float(amount), 2
    )
    account_info[desired_account] = globals()[desired_account].balance


def Close():
    desired_account = input("Enter Which Account You Would Like To Close: ")
    if desired_account not in account_info:
        print("This Account Doesn't Exist")
        return
    account_info.pop(desired_account)


def Clear_Terminal():
    erase = "\x1b[2K"
    up = "\033[1A"
    print((up + erase) * 9999, end="")


actions = {
    1: Create_Account,
    2: Check_Status,
    3: Deposit,
    4: Transfer,
    5: Withdraw,
    6: Close,
    7: Clear_Terminal,
}
account_info = {}
print("Welcome Back To A Very Good Bank Name! How Can I Help You?")
while True:
    user_input = input(
        "Action 1. Create An Account 2. Check Status Of An Account 3. Deposit 4. Transfer 5. Withdraw 6. Close 7. Clear Terminal: "
    )
    if user_input in list(map(str, list(actions))):
        user_input = int(user_input)
        action = actions.get(user_input)
        action()
    else:
        print("Invalid Input")
