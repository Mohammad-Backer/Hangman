import random as rand

def word():
    """
    The function opens the file words.txt and reads it, in order to obtain a list of words called lines.
    It then chooses a random word from the list and splits it into its characters and return a list of the
    charachters composing the word.

    Returns:
    --------
    word_characters: List
    A List of the characters composing the randomly chosen word.
        
    """
    with open('words.txt') as f:
        lines = f.readlines()
        f.close()
    word = rand.choice(lines)
    word = word.strip('\n')
    word_characters = [w for w in word]
    return word_characters

def pos(letter, words):
    """
    The function checks if the letter entered by the user is present in the word chosen by the computer.
    It then appen the letter index inside a letter_pos list.

    Parameters:
    -----------
    letter: String
    The letter entered by the user.

    words: List
    The word chosen by the computer.

    Returns:
    --------
    letter_pos : List
    A list of integers containing the indeces of the letter found in the word.

    """
    pos = 0
    letter_pos = []
    for w in words:
        if letter == w:
            letter_pos.append(pos)
            pos += 1
        else:
            pos +=1
    return letter_pos


def main():
    print("The computer has chosen a word. You have to try and guess it by entering one letter at a time!\nYou have 10 wrong guesses.")
    guesses = 10
    chosen_word = word()
    guessed = ["_" for i in range(len(chosen_word))]
    while True:
        if guessed == chosen_word:
            print(guessed)
            print("You have won!")
            break
        if guesses == 0:
            print("You have lost!")
            break
        print(guessed)
        user_input = input("Please enter a letter: ")
        if user_input.isalpha() and len(user_input) == 1:
            if user_input not in chosen_word:
                print("You guessed wrong!")
                guesses -= 1
                print("You still have", guesses, "guesses!")
            else:
                positions = pos(user_input, chosen_word)
                for j in positions:
                    guessed[j] = user_input


if __name__ == "__main__":
    main()