def get_word():
    user_word = input("Player 1, enter your word:")
    user_word = user_word.upper()
    if not all(x.isalpha() or x.isspace() for x in user_word):
        print("This is not a valid word,try again")
        return get_word()
    print("\n"*2000)
    return user_word


def check_word(word1,word2):
    if word1 == word2:
        return True
    else:
        return False

def hide_word(word1):
    hidden = ""
    for c in word1:
        if c.isalnum():
            c = c.replace(c,"*")
        hidden += c
    return hidden

def is_valid(letter):
    if len(letter) == 1 and letter.isalpha():
        return True
    else:
        return False

def checker(letter,original,hidden):
    i = 0
    j = 0
    for char in original:
        if char == letter:
            hidden[i] = char
            j = 1
        i += 1
    if j == 0:
        return False
    return ("".join(hidden))
