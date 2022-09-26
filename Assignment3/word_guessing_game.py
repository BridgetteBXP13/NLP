'''
Welcome to word_guessing_game.py! Created by Bridgette Bryant, netID: BMB180001
Created for Assignment 3 of 4395.001 Human Language Technologies in order to
familiarize myself with ....

REQUIRED PARAMETERS:


This programs......

Input...

Output...

Classes....

Functions...'''

import sys                                  # to get the system parameter (anat19.txt)
import os                                   # used to get the os system for anat19.txt
import pickle                               # used for saving/reading the finished
from nltk.corpus import stopwords           # used to remove the stopwords from the raw text tokens
from nltk.stem import WordNetLemmatizer     # used to get the lemmas oad

# Classes

# Functions

# Reads in the parameter data file from the file directory, works with different OS systems
def readdatafile(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    return text_in

def calcLexicalDiversity(token_text):
    return

def printNumLemmas():
    return

def processRawText(raw_text):
    # Lowercase raw text
    # Tokenize raw text
    # Remove non-alpha, stopword, and less than length 5 tokens
    # lemmatize the tokens
    # Create a set of unique lemmas
    # Pos tagging on unique lemmas
    # Print first 20 tagged items
    # Create list of only noun lemmas
    # Print number of tokens (inital)
    # Print number of nouns
    # Return the tokens and nouns

def guessingGame(nouns):
    # Print game rules/instructions
    # Give user starting 5 points
    # Play game while user hasn't hit negative points or they guessed '!' as a letter
    # randomly choose 1 of the 50 word in the top 50 list, remove the ones as they have
    # already been used
    # Output to console the underscores for each letter in the word
    # Ask the user for a letter, verify they haven't guessed it already for this word
    # if letter is in the word, and hasn't been guessed before, print 'Right'
    # Fill in the matching letter and add 1 point to their score
    # If letter is in the word, but has already been guessed, subtract 2 from their score
    # If letter not in word, and they haven't guessed it before subtract 1 from their score
    # print "Sorry, guess again"
    # If letter not in word, and they have guessed it already , subtract 3 from their score
    # Keep track of cumulative score, if score negative end game, if entered letter is '!', end game
    # Give user feedback based on score after each guess

# the main driver
if __name__ == '__main__':
    # Verifying that the system parameter 'data/anat19.txt is in place
    if len(sys.argv) < 2: # If not print an error message
        print('Please setup the parameter \'data/anat19.txt\'')
        print('Exiting...')
    else: # If so, continue
        fp = sys.argv[1]
        fileData = readdatafile(fp) # Read the file using the readdatafile function

    # Calculate lexical diversity

    # Write function to preprocess raw text

    # Create a dictionary of {noun:count of noun in tokens}

    # Sort the dictionary by count

    # Print the 50 most common words and their counts

    # Save those words to a list

    # Make guessing game function
