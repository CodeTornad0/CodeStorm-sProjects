from translate import Translator
import languageRunner


while True:
    FromLanguage = input(
        "Enter The Language You'll Will Be Writing In [Enter ? For Help]: "
    )
    text = input("Enter The Text To Be Translated: ")
    ToLanguage = input("Enter The Language To Be Converted To [Enter ? For Help]: ")
    while ToLanguage.strip() == "?" or FromLanguage.strip() == "?":
        languageRunner.Help()
        if ToLanguage.strip() == "?":
            ToLanguage = input("Enter Language To Be Converted To [Enter ? For Help]: ")
        else:
            FromLanguage = input(
                "Enter The Language You Will Be Writing In [Enter ? For Help]: "
            )
    translator = Translator(from_lang=FromLanguage, to_lang=ToLanguage)
    translation = translator.translate(text)
    print(translation)
