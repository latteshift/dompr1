# Problem Set 2, hangman.py
# Name: Yeva Marchenko
# Collaborators:
# Time spent: 7 days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    return set(secret_word).issubset(set(letters_guessed))




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    answer = ""

    for letter in secret_word:
      if letter in letters_guessed:
        answer = answer + letter
      else:
        answer = answer + "_ "

    return answer





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remaining_letters = ""
    for i in string.ascii_lowercase:

      if i not in letters_guessed:
        remaining_letters = remaining_letters + i

    return remaining_letters  

    
 
 


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = set()
    print("Welcome to the game Handman! \nI am thinking about the word which is", len(secret_word), "letters long. \n-----------------------\nYou have", guesses_remaining, "guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))

    while guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("----------------------- \nYou have", guesses_remaining, "guesses left.\nAvailable letters:", get_available_letters(letters_guessed))

        taking_guesses = input("Please guess a letter:\n").lower()

      #when the letters are symbols 
        if not taking_guesses.isalpha():
          warnings_remaining = warnings_remaining-1
          print("Oops! That is not a valid letter. You have", warnings_remaining," warnings left.")

      #the letter is guessed 
        if taking_guesses in secret_word:
          letters_guessed.add(taking_guesses)
          print("Good guess.")

        #the letter is not guessed
          #the letter is a vowel
        if taking_guesses in "aeiou" and taking_guesses not in secret_word:
              guesses_remaining = guesses_remaining-2
              print("Oops! That letter is not in my word.")
          #the letter is not a vowel
        elif taking_guesses not in secret_word:
              guesses_remaining = guesses_remaining-1
              print("Oops! That letter is not in my word.")

        #the letter is guessed twice
        elif taking_guesses in letters_guessed:
          print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left.")

        #ran out of warnings
        if warnings_remaining == 0:
          print("You have run out of warnings. You lose one guess.")
          guesses_remaining = guesses_remaining-1
        


        print(get_guessed_word(secret_word, letters_guessed))

    if guesses_remaining <= 0:
        print("Sorry, you have run out of guesses. The word was", secret_word)
    else:
        print("Congratulations, you won! Your total score for this game is", len(set(secret_word)) * guesses_remaining) 


      

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    else:
        for i, letter in my_word:
            if letter == '_':
                if other_word[i] in my_word:
                    return False  
            else:
                if my_word[i] != other_word[i]:
                    return False              
        return True

    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''


  
    possible_letters = []
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word):
        possible_letters.append(other_word)      
    if len(possible_letters) == 0:
      return "No matches found."
    else:
      return possible_letters



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []
    print("Welcome to the game Handman! \nI am thinking about the word which is", len(secret_word), "letters long. \n-----------------------\nYou have", guesses_remaining, "guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))

    while guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("----------------------- \nYou have", guesses_remaining, "guesses left.\nAvailable letters:", get_available_letters(letters_guessed))


        print("Available letters: ", get_available_letters(letters_guessed))
        
        taking_guesses = input("Please guess a letter:\n").lower()

        if taking_guesses.isalpha() == True: 
          if len(taking_guesses) == 1 or taking_guesses == "*":
            if taking_guesses == "*":
                print("Possible word matches are: ", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

            if taking_guesses not in letters_guessed:

                letters_guessed.append(taking_guesses)

                lttrs = False 
                for i in secret_word:
                    if i in taking_guesses:
                        lttrs = True
                        print("Good guess: ", end='')
                        break
                if lttrs == False:
                    print("Oops! That letter is not in my word. ")


                    if taking_guesses in 'aeiou':
                        guesses_remaining = guesses_remaining - 2 
                    else:    
                        guesses_remaining = guesses_remaining - 1
            else:
                if warnings_remaining > 0:
                    warnings_remaining = warnings_remaining - 1
                    print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left: ")
                else:
                    print("Oops! That is not a valid letter. You don't have any warnings left: ")  

        else:
          if warnings_remaining >0:
              warnings_remaining = warnings_remaining - 1
              print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left: ")
          else:
              print("Oops! That is not a valid letter. You don't have any warnings left: ")
        print(get_guessed_word(secret_word, letters_guessed))

    if guesses_remaining <= 0:
        print("Sorry, you have ran out of guesses. The word was", secret_word)  
    else:
        print("Congratulations, you won! Your total score is:", guesses_remaining * len(secret_word))





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

# ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

