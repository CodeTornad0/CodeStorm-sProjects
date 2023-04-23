while True:
    userInput = input('Would You Like To 1. Convert Binary To Text Or 2. Convert Text To Binary: ')
    if userInput.isdigit():
        userInput = int(userInput)
        if userInput == 1:
            userInput = input('Enter Binary Text: ')
            if userInput.isdigit():
                result = ''
                while userInput:
                    result += chr(int(userInput[:8], 2))
                    userInput = userInput[8:]
                print(f'Converted Answer:', result)
            else: print('Invalid Input')
        elif userInput == 2:
            userInput = input('Enter Text: ')
            result = ''.join(format(ord(i), '08b') for i in userInput)
            print('Converted Result:', str(result))
        else:
            print('Invalid Input')
    else: print('Invalid Input')