def handle_conversion_type(prompt, options):
    response = input(f"{prompt}: ")
    while response.strip().lower() not in options:
        print("Invalid Conversion. Please try again")
        response = input(f"{prompt}: ")
    return response.strip().lower()


def convert(input_text, mapping_dictionary):
    output_text = ""
    for char in input_text:
        output_text += mapping_dictionary.get(char, char)
    return output_text


def create_conversion_map(conversion_method):
    if conversion_method == "numbers":
        return {
            "0": "D",
            "1": "I",
            "2": "Z",
            "3": "E",
            "4": "h",
            "5": "S",
            "6": "g",
            "7": "L",
            "8": "B",
            "9": "G",
        }
    # if conversion_method == "characters"
    return {
        "O": "0",
        "D": "0",
        "I": "1",
        "Z": "2",
        "E": "3",
        "h": "4",
        "S": "5",
        "g": "6",
        "L": "7",
        "B": "8",
        "G": "9",
    }


conversion_type = handle_conversion_type(
    "Would you like to convert numbers into characters [numbers] or characters into numbers [characters]",
    ["numbers", "characters"],
)
text = input("Enter the text you would like to convert: ")
conversion_map = create_conversion_map(conversion_type)
print(convert(text, conversion_map))
