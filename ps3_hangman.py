# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/davidxiong/Desktop/words.txt"

def loadWords():
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
    print("   ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False
        else:
            return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    a = []
    for i in list(secretWord):
        if i in lettersGuessed:
            a.append(i)
        else:
            a.append('_')
    return ''.join(a)
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in lettersGuessed:
        if i in alphabet:
            alphabet.remove(i)
        else:
            alphabet = alphabet
    return ''.join(alphabet)

            

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, my friend')
    print('Please give one guess of one word that you think may contain in the word list')
    times = 8
    lettersGuessed = []
    
    while times >0:
        print("You have " + str(times) + "left.")
        print("Available letters:" + getAvailableLetters(lettersGuessed))
        
        while True:
            guessletter = str(input("Please guess again:")).lower()
            if guessletter in lettersGuessed:
                print("You have already guessed this letter" + getGuessedWord(secretWord, lettersGuessed))
                print("You have " + str(times) +" times left.")
                print("Availabel letters:" + getAvailableLetters(lettersGuessed))
            else:
                break
            lettersGuessed += guessletter
            
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good Guess:" + getGuessedWord(secretWord, lettersGuessed))
            print("You win the game!")
        elif guessletter in secretWord:
            print("Good Guessed:" + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("That word is not in my word" + getGuessedWord(secretWord, lettersGuessed))
            times-=1
            
        if times ==0:
            print("You lose the game")
            
        
        
            
            
  
            
        
        
        
    
    
    
    
    
    
    
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
