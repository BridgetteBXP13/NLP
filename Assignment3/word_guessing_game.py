'''
Welcome to word_guessing_game.py! Created by Bridgette Bryant, netID: BMB180001
Created for Assignment 3 of 4395.001 Human Language Technologies in order to

REQUIRED PARAMETERS:
    You must have a folder in the same directory named 'data' containing the
    text data file named 'anat19.txt' it can be found here under Assignment 3:
    https://bridgettebxp13.github.io/CS-4395.001---Human-Language-Technologies

    or here as this github in Assignment 3:
    https://gihub.com/BridgetteBXP13/CS-4395.001---Human-Language-Techologies
Without the directory/file above the program will simply display an error message
telling you that your are missing the parameters and quit.



This program was designed to practice data processing from a text file, creating tokens, lemmatizing, getting unique
lemmas, making a dictionary of lemmas by count, calculate lexical diversity, and creating a list of nouns from the
tagged nouns. After preprocessing text it will create a list of top 50 nouns and use them for the guessing game. The
game has the following rules/how to play:

    1. You will be given a word (each letter designated by an underscore
    2. You will start off with 5 points, to keep playing you must keep your score above 0!
    3. If you guess a correct letter, you will gain 1 point, and the letters will be revealed.
    4. If you guess a correct letter you have already guessed, you will lose 2 points!
    5. If you guess an incorrect letter you haven't guessed before, you will lose 1 point!
    6. If you guess an incorrect letter you have already guessed, you will lose 3 points!
    7. If you want to quit, enter '!' as a letter.
    8. Try to see how long you last and how many words you can guess!

The game will operate with the rules/how to play above, if the user guesses all the words it will congratulate them.
Or it they quit it will output the ending score, number of words guessed, and the words guessed to the user. It will
also thank the user for playing.


Functions:

readdatafile:
    This function reads in the parameter data file from the file directory, works with different OS systems. It is
    utilized by main to read the program's given parameters.

printnumtags:
    This function takes a list of tags and a number, it will print the first num of tags in the list. It is utilized by
    processrawtext to print 20 tags.

processrawtext:
    This function processes our raw text into text_tokens and unique noun lemmas and returns them.
    It is utilized by main to process the input from the anat19.txt file.

chooseword:
    This function takes a list of nouns, and randomly chooses a noun. Then removes such noun from the list.
     After it returns the chosen noun and the updated noun list. It is utilized by guessinggame.

guessinggame:
    This function runs the guessing game part of this program. It requires a list of nouns. First it will print
    rules and how to play to the user. Then it will continue to give the user words to guess (designated by
    underscores). The user will be prompted to guess a letter, if not given a letter it will continue to ask them to
    guess again. If the user inputs a letter it will assign appropriate letters to the word and add/subtract the
    appropriate amount of points according to the rules/how to play. If the user manages to guess all the words the
    game ends and the user will be congratulated as a guessing master. If the user quits by entering a '!' the function
    will print the end sequence and thank them for playing. The end sequence for both is displaying the ending number of
    points, number of guessed words, and the guessed words. The program will then return to main.
main:
    Verifies that the parameter data file anat19.txt is present (using readdatafile). Then it will use the
    processrawdata function to process the given raw text. Then it will calculate/print the lexical diversity of
    the return tokens/lemmas from processrawdata. After it will create a dictionary of the unique lemmas and sort them
    by their count. Next it prints and saves the first 50 nouns to a list. Finally it calls the guessinggame function to
    start the game with the given list of nouns.
'''

import sys                                  # to get the system parameter (anat19.txt)
import os                                   # used to get the os system for anat19.txt
import random                               # used to randomly select from the list
import nltk                                 # Used for the following
from nltk import word_tokenize              # used to tokenize the data by word
from nltk.corpus import stopwords           # used to remove the stopwords from the raw text tokens
from nltk.stem import WordNetLemmatizer     # used to get the lemmas


# Functions

# Reads in the parameter data file from the file directory, works with different OS systems
def readdatafile(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    return text_in
# Given a list of tags and a number, it will print the first num of tags in the list
def printnumtags(tags_list, num):
    count = 0   # Set count to 0
    # For every tag in list
    for t in tags_list:
        print(t)    # Print the tag
        count += 1  # Add 1 to count
        # If we have hit num, break the loop
        if count == num:
            break
    return
# Prepocceses our raw text into text_tokens and unique noun lemmas and returns them
def processrawtext(raw_text):
    # Lowercase raw text
    raw_text = raw_text.lower()
    # Tokenize raw text
    text_tokens = word_tokenize(raw_text)
    # Remove non-alpha, stopword, and less than length 5 tokens
    text_tokens = [t for t in text_tokens if t.isalpha() and t not in stopwords.words('english')]
    text_tokens = [t for t in text_tokens if len(t) >= 5]
    # lemmatize the tokens
    wnl = WordNetLemmatizer()
    text_lemmas = [wnl.lemmatize(t) for t in text_tokens]
    # Create a set of unique lemmas
    unique_text_lemmas = list(set(text_lemmas))
    # Pos tagging on unique lemmas
    text_tags = nltk.pos_tag(unique_text_lemmas)
    # Print first 20 tagged items
    printnumtags(text_tags, 20)
    # Create list of only noun lemmas
    noun_lemmas = [ t for t in text_tags if t[1] == 'NN' or t[1] == 'NNS' or t[1] == 'NNP']
    # Print number of tokens (inital)
    print("Number of initial tokens: ", len(text_tokens))
    # Print number of nouns
    print("Number of nouns: ", len(noun_lemmas))
    # Return the tokens and nouns
    return text_tokens, noun_lemmas

# Takes a list of nouns, randomly chooses a noun, removes such noun from the list, and then returns them both
def chooseword(nouns):
    # Randomly chose a word from the given nouns
    word = random.choice(nouns)
    # Remove the choosen word from the nouns
    nouns.remove(word)
    # Return the word and list of nouns
    return word, nouns

# Runs the guessing game, requires a list a nouns, displays the rules/points/game progress to the user.
# Manages the user's input and game logic.
def guessinggame(nouns):
    # Print game rules/instructions
    print("\n\n\n\n\n\nWelcome to Word Guessing Game!")
    print("\nHow to Play:")
    print("1. You will be given a word (each letter designated by an underscore)")
    print("2. You will start off with 5 points, to keep playing you must keep your score above 0!")
    print("3. If you guess a correct letter, you will gain 1 point, and the letters will be revealed.")
    print("4. If you guess a correct letter you have already guessed, you will lose 2 points!")
    print("5. If you guess an incorrect letter you haven't guessed before, you will lose 1 point!")
    print("6. If you guess an incorrect letter you have already guessed, you will lose 3 points!")
    print("7. If you want to quit, enter '!' as a letter.")
    print("8. Try to see how long you last and how many words you can guess!\n\n\n")
    # Give user starting 5 points
    points = 5
    cur_char = '.'
    cur_word = ""
    cur_word_progress = ""
    guessed_letters = []
    guessed_words = []
    word_found = True
    # Play game while user hasn't hit negative points or they guessed '!' as a letter
    while points > 0 and not cur_char == "!":
        # If they have guessed the current word, generate a new one:
        if word_found:
            # Reset the bool
            word_found = False
            # Reset the guessed letters
            guessed_letters = []
            # Reset the word progress
            cur_word_progress = ""
            # Make sure there is a new word available in the list
            if len(nouns) < 1:
                print("You've guessed all the words!")
                print("Congratulations you are a word guessing master!")
                break
            # randomly choose 1 of the 50 word in the top 50 list, remove the ones as they have already been used
            cur_word, nouns = chooseword(nouns)
            for i in cur_word:
                cur_word_progress += "_"
        # Output to console the underscores for each letter in the word and guessed letters
        print(cur_word_progress)
        # Ask the user for a letter, verify they haven't guessed it already for this word
        cur_char = input("\nPlease input a letter to guess: ")

        # Verify that input is not a '!'
        if cur_char == '!':
            print("\nThank you for playing!")
            print("Current Score: ", points)
            print("Number of Guessed Words: ", len(guessed_words))
            print("Guessed Words: ", guessed_words)
            # Reset the guessed letters
            guessed_letters = []
            break

        # Verify that the input is a single letter
        if not cur_char.isalpha():
            print("Entered: " + cur_char + " which is not a letter or a '!', please try again.")
            continue
        # if letter is in the word, and hasn't been guessed before, print 'Right'
        if cur_char in cur_word and cur_char not in guessed_letters:
            # Fill in the matching letter and add 1 point to their score
            for i in range(len(cur_word)):
                if cur_char == cur_word[i]:
                    cur_word_progress = cur_word_progress[:i] + cur_char + cur_word_progress[i+1:]
            points += 1
            print("Right! Gain 1 point!")
            print("Current Points: ", points)
            guessed_words.append(cur_char)
            # Double check that they didn't guess the last letter
            if '_' not in cur_word_progress:
                print("You've guessed the word!")
                print("Number of Guessed Words: ", len(guessed_words))
                print("Guessed Words: ", guessed_words)
                guessed_words.append(cur_word)
                # Set the bool to true
                word_found = True
                # Reset the guessed letters
                guessed_letters = []
                print("\n")
        elif cur_char in cur_word: # If letter is in the word, but has already been guessed, subtract 2 from their score
            # Deduct 2 points
            points -= 2
            print("You've already guessed that, it's even in the word! Lose 2 points!")
            print("Current Points: ", points)
        elif cur_char not in guessed_letters: # If letter not in word, and they haven't guessed it before subtract 1 from their score
            points -= 1
            print("Sorry, guess again! Lose 1 point.")
            print("Current Points: ", points)
            guessed_letters.append(cur_char)
        else: # If letter not in word, and they have guessed it already, subtract 3 from their score
            points -= 3
            print("Incorrect, and you've already guessed that letter! Lose 3 points!")
            print("Current Points: ", points)

        # If score negative end game
        if points < 0:
            print("\nSorry you've run out of points.")
            print("Thank you for playing!")
            print("Current Score: ", points)
            print("Number of Guessed Words: ", len(guessed_words))
            print("Guessed Words: ", guessed_words)
            break
    # Reset the values
    points = 5
    cur_char = '.'
    cur_word_progress = ""
    guessed_letters = []
    guessed_words = []
    word_found = True
    return

# the main driver
if __name__ == '__main__':
    # Verifying that the system parameter 'data/anat19.txt is in place
    if len(sys.argv) < 2: # If not print an error message
        print('Please setup the parameter \'data/anat19.txt\'')
        print('Exiting...')
    else: # If so, continue
        fp = sys.argv[1]
        fileData = readdatafile(fp) # Read the file using the readdatafile function

    # Process the raw text using the processRawText function, get the text_tokens and noun lemmas
    text_tokens, noun_lemmas = processrawtext(fileData)
    # Calculate and print the lexical diversity
    print("\nLexical Diversity: %.2f" % (len(noun_lemmas) / len(text_tokens)))
    # Create a dictionary of {noun:count of noun in tokens}
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in text_tokens]
    counts = {t:lemmas.count(t) for t in noun_lemmas}
    # Sort the dictionary by count
    sorted_count = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # Print the 50 most common words and their counts, and save those words to list common_list
    print("\n50 most common words:")
    common_list = []
    for i in range(50):
        print(sorted_count[i][0][0])
        common_list.append(sorted_count[i][0][0])
    # Make guessing game function
    guessinggame(common_list)

