import numpy


def Check_Number(number, name):
    while number.isdigit() is False:
        print("Enter An Integer")
        number = input(f"{name}: ")
    return int(number)


explanation = """Your Array Was Able To Print, But It Didn't Display All Of The
Characters Because Your Values Were Too Big. The Maximum Amount Of Items That 
Can Be Put Into An Array Is 992. That Means You Can Do Any Variation Of rows x 
columns = 992. An Example Of This Is 32 x 31 = 922. If I Were To Increase Any 
Of These Numbers, It Won't Print"""
character = input("Character: ")
rows = input("Rows: ")
rows = Check_Number(rows, "Rows")
columns = input("Columns: ")
columns = Check_Number(columns, "Columns")
try:
    array = (
        str(numpy.zeros((rows, columns)))
        .replace(".", "")
        .replace("0", character)
        .replace("[", "", 1)
    )
    array = array[:-1]
    print(f" {array}")
    characters = rows * columns
    actual = array.count(character)
    if actual < characters:
        print(explanation)
except ValueError:
    print("This Array Is Too Big Too Make")
