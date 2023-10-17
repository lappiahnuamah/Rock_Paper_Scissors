import string
test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]


def bleeper(word):
    pos = 0
    for character in word:
        if character not in string.punctuation:
            character = '*'
        word = word.replace(word[pos], character)
        pos += 1
    return word #

for word in test_words:
    print(bleeper(word))