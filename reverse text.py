def reverse(text):
    "reverses a given string"
    reversed_text = ''
    index = len(text) - 1

    while index >= 0:
        reversed_text += text[index]
        index -=1
    return reversed_text
