def Filter_Input(user):
    for char in characters_to_remove:
        if char in user:
            user = user.replace(char, "")
    if user.strip() == "":
        print("Invalid input")
        user = input("Enter text: ")
        user = Filter_Input(user)
    try:
        return user.split()
    except AttributeError:
        return user


word_counts = {}
characters_to_remove = [*"!@#$%^&*()-=_+[]{};':|,./?><" + '"' + "'"]
user_input = input("Enter text: ")
user_input = Filter_Input(user_input)
for word in user_input:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
print(
    f"The most common word(s) is (are) {[key for key, value in word_counts.items() if value == sorted(word_counts.values(), reverse=True)[0]]} at {sorted(word_counts.values(), reverse=True)[0]} instance(s)"
)
print(
    f"The least common word(s) is (are) {[key for key, value in word_counts.items() if value == sorted(word_counts.values())[0]]} at {sorted(word_counts.values())[0]} instance(s)"
)
print(
    f"The median word(s) is (are) {[key for key, value in word_counts.items() if value == sorted(word_counts.values())[len(word_counts) // 2]]} at {sorted(word_counts.values())[len(word_counts) // 2]} instance(s)"
)
input("Press enter or return to see all words")
choice = (
    input("Would you like to see it in a variable or printed out [v/p]: ")
    .strip()
    .lower()
)
while choice not in ["v", "p"]:
    print("Invalid choice")
    choice = (
        input("Would you like to see it in a variable or printed out [v/p]: ")
        .strip()
        .lower()
    )
if choice == "v":
    print(word_counts)
else:
    for word, count in word_counts.items():
        print(f'The word "{word}" appears {count} time(s)')
