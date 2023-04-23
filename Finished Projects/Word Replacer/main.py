def Replace_Words(text):
    target_word = input("What word do you want to replace: ")
    replacement_chars = input("What word will replace it: ")
    words = text.split()
    for i, word in enumerate(words):
        if word == target_word:
            words[i] = replacement_chars
    return " ".join(words)


input_text = input("Text: ")
result = Replace_Words(input_text)
print(result)
