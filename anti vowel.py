def anti_vowel(text):
    """Function removes the vowels from a given string"""
    word = "" #variable that contains every letter that is not a vowel
    for c in text:
        if c not in "aeiouAEIOU":
            word += c
    return word


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    """ Function simulates a simple scrabble game"""
    word = word.lower()
    word = word.replace(" ", "") #gets rid of the whitespaces in a word
    total = 0
    for c in word:
        total += score[c]
    return total

def censor(text, word):
    """Function censors given words in a partiular text"""
    wordlist = text.split()
    for i in range(0 , len(wordlist)):
        if wordlist[i] == word:
            wordlist[i] = "*" * len(word)
    return ' '.join(wordlist)

def purify(numbers):
    """Function removes all odd numbers from a given list of numbers"""
    evennums = []
    for num in numbers:
        if num % 2 == 0:
            evennums.append(num)
    return evennums

def median(numbers):
    """Function gets the median of a given list of numbers"""
    numbers = sorted(numbers)

    index1 = len(numbers) / 2
    index2 = len(numbers) / 2 - 1

    if len(numbers) % 2 == 0:
        return (numbers[(index1)] + numbers[(index2)]) / 2.0
    else:
        return numbers[(index1)]
