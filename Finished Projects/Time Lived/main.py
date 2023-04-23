from datetime import date
from calendar import monthrange
from dateutil import relativedelta


def Invalid_Input(user, question):
    while user.isdigit() is False or int(user) < 1:
        print("Invalid Input")
        user = input(question)
    return int(user)


def Exceeding_Limit(user, limit, question):
    while user > limit:
        print("Input Is Too Large")
        user = input(question)
        user = Invalid_Input(user, question)
    return int(user)


year = input("What is your birth date (year): ")
year = Invalid_Input(year, "What is your birth date (year): ")
month = input("What is your birth date (month): ")
month = Invalid_Input(month, "What is your birth date (month): ")
month = Exceeding_Limit(month, 12, "What is your birth date (month): ")
day = input("What is your birth date (day): ")
day = Invalid_Input(day, "What is your birth date (day): ")
day = Exceeding_Limit(
    day, monthrange(year, month)[1], "What is your birth date (day): "
)
today = date.today()
birthday = date(year, month, day)
difference = today - birthday
times = {
    "months": relativedelta.relativedelta(today, birthday).months
    + (relativedelta.relativedelta(today, birthday).years * 12),
    "weeks": int(difference.days / 7),
    "days": difference.days,
    "hours": difference.days * 24,
    "minutes": difference.days * 24 * 60,
    "seconds": difference.days * 24 * 60 * 60,
    "microseconds": difference.days * 24 * 60 * 60 * 1000,
}
print("You have lived")
for i in range(len(times)):
    print(list(times.values())[i], list(times.keys())[i])
