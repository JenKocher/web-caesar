def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lowercase = letter.lower()
    idx = alphabet.index(lowercase)
    return idx


def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.lower() in alphabet:
        if char.upper() == char:
            uppercase = True
        else:
            uppercase = False
        oldpos = alphabet_position(char)
        newpos = oldpos + rot
        if newpos > 25:
            newpos = newpos % 26
        newchar = alphabet[newpos]
        if uppercase:
            newchar = newchar.upper()
    else:
        newchar = char
    return newchar

def encrypt(message, rotation):
    newmessage = ''
    for char in message:
        newmessage = newmessage + rotate_character(char, rotation)
    return newmessage
