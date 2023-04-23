import random

user_input = input("Enter If You Dare... For Worthiness!!!")
chance = random.randint(1, 2)
if chance != 2:
    print("You're Not Who We Are Looking For")
    quit()
print("young rookie... ")
user_input = input("Press Enter For Worthiness")
chance = random.randint(1, 5)
if chance != 5:
    print("You Were Unwise To Go On Such A Journey")
    quit()
print("You Might Be Good")
user_input = input("Press Enter To Venture Forward")
chance = random.randint(1, 10)
if chance != 10:
    print("Almost...")
    quit()
print("You Have Proven Yourself... As Worthy!!!!")
