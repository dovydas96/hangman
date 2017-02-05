import Worked as wo

def get_word():
    user_word = input("Player 1, enter your word:")
    user_word = user_word.upper()
    if not all(x.isalpha() or x.isspace() for x in user_word):
        print("This is not a valid word,try again")
        return get_word()
    print("\n"*2000)
    return user_word

def main():
    original = get_word()
    hidden = wo.hide_word(original)

    seen = []
    i = 0
    while i <= 5:
        print("What is this word? {}".format(hidden))
        letter = input("Player 2, enter a letter:")
        letter = letter.upper()


        if wo.is_valid(letter):

            if letter in seen:
                print("You have already guessed this letter")

            elif (wo.checker(letter,original,list(hidden))):
                hidden = wo.checker(letter,original,list(hidden))
                seen.append(letter)
                if hidden == original:
                    print("Correct!\nThe word was {}".format(original))
                    quit()
                else:
                    print(hidden)

            else:
                print("Wrong guess!")
                print("You have {} guesses remaining".format(5-i))
                i += 1
        else:
            print("Invalid input")

    print("Game Over!\nThe word was {}".format(original))

if __name__ == "__main__":
    main()
