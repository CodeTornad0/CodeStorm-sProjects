import random
binaryLetters = ['01100001',
                 '01100010',
                 '01100011',
                 '01100100',
                 '01100101',
                 '01100110',
                 '01100111',
                 '01101000',
                 '01101001',
                 '01101010',
                 '01101011',
                 '01101100',
                 '01101101',
                 '01101110',
                 '01101111',
                 '01110000',
                 '01110001',
                 '01110010',
                 '01110011',
                 '01110100',
                 '01110101',
                 '01110110',
                 '01110111',
                 '01111000',
                 '01111001',
                 '01111010',
                 '01000001',
                 '01000010',
                 '01000011',
                 '01000100',
                 '01000101',
                 '01000110',
                 '01000111',
                 '01001000',
                 '01001001',
                 '01001010',
                 '01001011',
                 '01001100',
                 '01001101',
                 '01001110',
                 '01001111',
                 '01010000',
                 '01010001',
                 '01010010',
                 '01010011',
                 '01010100',
                 '01010101',
                 '01010110',
                 '01010111',
                 '01011000',
                 '01011001',
                 '01011010']
binaryResponse = '01001101 01111001 00100000 01110000 01100101 01101111 01110000 01101100 01100101 00100001 00100000 01010111 01100101 00100000 01101101 01100101 01100101 01110100 00100000 01100001 01100111 01100001 01101001 01101110 00100000 01100010 01110010 01101111 01110100 01101000 01100101 01110010 00101110'
def unknown():
    response = ['Could you re-phrase that?', '?', 'What does that mean?'][random.randrange(3)]
    return response