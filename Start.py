import Worked as wo

def main():
    original = wo.get_word()
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

                if wo.check_word(original,hidden):
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
