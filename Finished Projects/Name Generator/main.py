import random
import names


def Invalid_Input(option, category, option1, option2):
    while option not in ["1", "2"]:
        print("Invalid Option")
        option = input(f"{category} Type 1. {option1} 2. {option2}: ").strip()
    return option


def Generate_Email():
    email_type = input("Email Type 1. brand 2. casual: ").strip()
    email_type = Invalid_Input(email_type, "Email", "brand", "casual")
    domain = input("Domain: @")
    if email_type == "1":
        words = []
        brand = []
        repeats = random.randint(4, 8)
        with open("business.txt", "r") as f:
            for line in f.readlines():
                brand.append(line.rstrip())
        for i in range(repeats):
            if i == repeats - 1:
                words.append(random.choice(brand))
                break
            words.append(f"{random.choice(brand)}_")
        email = "".join([str(elem) for elem in words]) + f"@{domain}"
    else:
        added_numbers = ""
        name = names.get_full_name().replace(" ", "_")
        numbers = list(range(0, 10))
        repeats = random.randint(3, 5)
        for _ in range(repeats):
            added_numbers += str(random.choice(numbers))
        email = f"{name}_{added_numbers}@{domain}"
    print(f"Email: {email}")


def Generate_Name():
    sex = input("Sex Type 1. male 2. female: ").strip()
    sex = Invalid_Input(sex, "Sex", "male", "female")
    name = names.get_full_name("male" if sex == "1" else "female")
    print(name)


name_type = input("Name Type 1. email 2. name: ").strip()
name_type = Invalid_Input(name_type, "Name", "email", "name")
if name_type == "1":
    Generate_Email()
else:
    Generate_Name()
