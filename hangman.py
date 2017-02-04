'''

@author: Steve Denton

Variation of hangman.py. Text output only.

'''

import random


def fileToStringList(filename):
    """
    filename is a file of strings,
    returns a list of strings, each string represents
    one line from filename
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist


def getPossibleWords(wordlist, length):
    """
    returns a list of words from wordlist having a
    specified length
    """
    newWordlist = []
    
    for word in wordlist:
        if(len(word) == length):
            newWordlist.append(word)
    
    return newWordlist


def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(wordList)


def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as word
    '''
    return ['_'] * len(word)


def updateLetter(guessList, wordToGuess, letter):
    '''
    wordToGuess is the word the user is trying to guess.
    guessList is the word to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed.

    Modify guessList to include letter in its proper locations if
    letter is in wordToGuess.

    For example, if the wordToGuess is "baloney" and so far only a and
    e have been guessed, then guessList is ['_','a','_','_','_','e','_']
    If letter is 'o', then guessList is modified to now be:
    ['_','a','_','o','_','e','_']

    '''
    flag = 'false'
    
    for i in range(0, len(wordToGuess)):
        if(wordToGuess[i] == letter):
            guessList[i] = letter
            flag = 'true'
    
    return flag
    
def getGuessLength():
    '''
    
    returns an integer of the length of the word to guess
    only if the length is 3 or greater
    
    '''
    length = int(input("how many letters in word to guess? "))
    
    # check guessLength
    if(length < 3):
        print("Sorry, the word length must be at least 3 characters.")
        getGuessLength()
          
    return length    


def guessWord(wordToGuess):
    '''
    
    returns a boolean value true if the word entered
    matches the given string
    
    '''
    word = input("enter word: ")
    flag = 'true'
    
    for i in range(0, len(wordToGuess)):
        if(wordToGuess[i] != word[i]):
            flag = 'false'
            if(flag == 'false'):
                break   
    
    return flag

def updateAlphabet(unusedLetters, letter):
    '''
    
    returns a new alphabet string with the last
    used character missing
    
    '''
    newString = unusedLetters
    
    for i in range(0, len(unusedLetters)):
        if(unusedLetters[i] == letter):
            newString = unusedLetters.replace(unusedLetters[i], "")
    
    return newString


def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    # setup for game
    guessLength = getGuessLength()
    guessesLeft = int(input("how many wrong letter guesses: "))
    print("")
    wordsOfLength = getPossibleWords(words, guessLength)
    wordToGuess = random.choice(wordsOfLength)
    guessList = guessStart(wordToGuess)
    unusedLetters = "abcdefghijklmnopqrstuvwxyz"

    # start the guessing
    while True:
        if guessList.count('_') == 0 or guessesLeft == 0:
            # all letters guessed
            break
        print("guessed so far:", displayGuess(guessList))
        print("letters not guessed: ", unusedLetters)
        print("number of misses left: ", guessesLeft)
        letter = input("guess a letter or enter + to guess word: ")
        if(letter == '+'):
            if(guessWord(wordToGuess) == 'false'):
                break
            else:
                for i in range(0, len(wordToGuess)):
                    guessList[i] = wordToGuess[i]
        elif(updateLetter(guessList, wordToGuess, letter) == 'false'):
            guessesLeft -= 1
            unusedLetters = updateAlphabet(unusedLetters, letter)
        else:
            unusedLetters = updateAlphabet(unusedLetters, letter)
                    
    # game over
    if guessList.count('_') == 0:
        print("You win. You guessed the word", wordToGuess)
    elif(guessesLeft == 0):
        print("You lost, you ran out of guesses. Word was:", wordToGuess)
    else:
        print("You guessed the wrong word. Word was:", wordToGuess)


if __name__ == '__main__':
    words = fileToStringList('lowerwords.txt')
    playGame(words)
