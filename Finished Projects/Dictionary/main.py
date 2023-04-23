from PyDictionary import PyDictionary

dictionary = PyDictionary()
word = input("Enter a word: ")
definition = dictionary.meaning(word)

if definition:
    indexes = len(list(definition.keys()))
    print(f"The definition of the word '{word}' is:")
    for i in range(indexes):
        print(f"{list(definition.keys())[i]}: {definition[list(definition.keys())[i]]}")
        print()
else:
    print("Word not found")
