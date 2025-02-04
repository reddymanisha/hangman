import random
from Words import words
import string

def get_valid_word(words):
    word = random.choice(words)       #randomly chooses word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)      #Letters in the word(already guessed)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()          #What the user has guessed

    #for limited chances giving lives
    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used 
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        #what current word is( i.e W _ R D) with dashes where the characters they haven't guessed are
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ''.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:   #if it is a valid alphabet which is not used
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1     #takes away a life , if wrong
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You've already used that character.Please try again.")

        else:
            print("Invalid character.Please try again")


#Gets here when len(word_letters) == 0 OR when lives==0
    if lives == 0:
        print("You died,sorry.The word was",word)
    else:
        print("You guessed the word", word,"!!")
    
hangman()