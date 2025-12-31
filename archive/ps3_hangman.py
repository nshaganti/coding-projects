# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l in lettersGuessed:
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    current_guess = secretWord
    for l in secretWord:
        if l in lettersGuessed:
            continue
        else:
            current_guess = current_guess.replace(l,'_ ')
    return current_guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = string.ascii_lowercase
    for l in lettersGuessed:
        if l in available:
            available = available.replace(l,'')
    return available    

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
    secretWord = secretWord.lower()
    print("Welcome to the game, Hangman!")
    print("I'm thinking of a word that is {} letters long".format(len(secretWord)))
    print("------------")
    
    lettersGuessed = []
    mistakesMade = 0
    
    while mistakesMade <= 8:
        if isWordGuessed(secretWord,lettersGuessed):
            print("Congratulations, you won!")
            break
        print("You have {} guesses left".format(8-mistakesMade))
        print('Available Letters: {}'.format(getAvailableLetters(lettersGuessed)))     
        guessedLetter = raw_input('Please guess a letter: ')
        if guessedLetter in secretWord:
            if guessedLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord,lettersGuessed)))
                print("------------")
            else:
                lettersGuessed.append(guessedLetter)
                print("Good guess: {}".format(getGuessedWord(secretWord,lettersGuessed)))
                print("------------")
            
        else:
            if guessedLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord,lettersGuessed)))
            else:
                mistakesMade = mistakesMade + 1
                print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord,lettersGuessed)))
                lettersGuessed.append(guessedLetter)
            print("------------")
            if mistakesMade >= 8:
                print('Sorry, you ran out of guesses. The word was {}'.format(secretWord))
                break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
