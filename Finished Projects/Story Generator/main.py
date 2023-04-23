import random

when = ["A few years ago", "Yesterday", "Last night", "A long time ago", "Today"]
who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]
name = """
Olivia	Noah
Emma	Liam
Amelia	Oliver
Ava	Elijah
Sophia	Mateo
Isabella	Lucas
Luna	Levi
Mia	Asher
Charlotte	James
Evelyn	Leo
Harper	Grayson
Nova	Luca
Scarlett	Ezra
Aurora	Ethan
Ella	Aiden
Mila	Wyatt
Aria	Sebastian
Ellie	Mason
Gianna	Benjamin
Sofia	Henry
Layla	Jack
Violet	Jackson
Willow	Hudson
Lily	Daniel
Hazel	Owen
Avery	Alexander
Camila	Maverick
Chloe	Kai
Elena	Carter
Paisley	Gabriel
Eliana	William
Penelope	Logan
Eleanor	Michael
Ivy	Samuel
Elizabeth	Muhammad
Isla	Waylon
Riley	Ezekiel
Abigail	Jayden
Nora	Luke
Stella	Theo
Zoey	Lincoln
Grace	Josiah
Emily	Jacob
Leilani	Elias
Emilia	Jaxon
Kinsley	David
Everly	Theodore
Delilah	Julian
Athena	Isaiah
Naomi	
"""
name = name.split()
residence = ["Barcelona", "India", "Germany", "Venice", "England"]
went = ["cinema", "university", "store", "school", "the office"]
happened = [
    "made a lot of friends",
    "ate a burger",
    "found a secret key",
    "solved a mystery",
    "wrote a book",
]
print(
    random.choice(when)
    + ", "
    + random.choice(who)
    + f" called {random.choice(name)}"
    + " who lives in "
    + random.choice(residence)
    + " went to the "
    + random.choice(went)
    + " and "
    + random.choice(happened)
    + "."
)
