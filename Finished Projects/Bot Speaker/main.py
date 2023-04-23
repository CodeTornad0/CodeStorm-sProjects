import os

import languages
from gtts import gTTS
from playsound import playsound

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
while True:
    accent = input(
        "Enter The Accent You Want The Speaker To Have [Enter ? For Help]: "
    ).strip()
    while accent == "?":
        languages.Help()
        accent = input(
            "Enter The Accent You Want The Speaker To Have [Enter ? For Help]: "
        ).strip()
    try:
        output = gTTS(text="error handling for accents", lang=accent, slow=False)
    except ValueError:
        print(
            "This Accent Is Not Supported Or You Didn't Use The Abbreviated Two Letter Characters For The Accent"
        )
    bot_text = input("Enter The Text You'll Be Listing To: ")
    name = input(
        "Enter The Name Of The Audio File [Enter Nothing For The Default Name]: "
    )
    if name.strip() == "":
        name = "python_text_to_speech"

    output = gTTS(text=bot_text, lang=accent, slow=False)
    output.save(f"{FILE_PATH}/{name}.mp3")
    playsound(f"{FILE_PATH}/{name}.mp3")
