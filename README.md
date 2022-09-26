
## Overview of Natural Language Processing (NLP)
[Here](Overview%20of%20NLP.pdf) is a lovely pdf which shows a brief overview of NLP.

## Assignment 1: Text Processing with Python

[Here](/Assignment1/create_emp_dict.py) is the code and the [data](/Assignment1/data/data.csv) (required for input).

This Program takes one input file data.csv in a given data folder. It then processes the data and
displays it in an organized employee list in the terminal, and also saves it as a dictionary in a
pickle file 'employeeList.p'. To use this program you simply need to create the following data file
in a /data directory as shown below and make sure it is set as a parameter in your IDE. Also, make
sure your data.csv file is in the appropriate format as shown below, from there you can run the 
program with the given inputs, add your own, and give the program input as it requests. Enjoy!

Created for Assignment 1 of 4395.001 Human Language Technologies in order to familiarize myself with python,
including simple file/data processing.

### REQUIRED PARAMETERS:    
                        You must have a folder in the same directory
                        name 'data' containing a file named 'data.csv'
                        it can be found [here](https://bridgettebxp13.github.io/CS-4395.001---Human-Language-Technologies/) under Assignment1, or [here](https://github.com/BridgetteBXP13/CS-4395.001---Human-Language-Technologies/) at this github in Assignment1.
                        
Without the directory/file above the program will simply give you an error message telling you that
you are missing the parameters!

This program takes a data.csv file as described above in the form:
Last,First,Middle Initial,ID,Office phone
Smith,Smitty,S,WH1234,5557771212
...

A list of employees with their primary information, it then processes the data file, creates Person object, and
inserts that person object into a dictionary based on their ID.

It gives the User opportunities to fix errors in employee IDs and Phone Numbers recursively. 

Some of the benefits of using Python for text processing is the simplicity of not having a lot of overhead when trying to do something very simple with the input file text. It also gives many options with the provided functions in libraries such as re and many built in functions such as .isdigit(), .isalpha(), .split(), and even .capitalize() which allowed me to avoid having to write unneccessary functions. Although I did find a couple weaknesses that Python doesn't support a lot of built in functions for dictionaries such as .hasKey() or .contains() that Java/C++ tend to have. Throughout this assignment I had a lot of python review and remembered basic data input/processing. I had to continuously remind myself that I didnt need variable declarations such as int i = 0, and deleted many semicolons along the process. I learned the different ways you can manipulate strings and list for data cleaning in python in the given fucntions mentioned above. 

Here is the [code](helloworld.py) and simple [documentation](helloworld.txt).

## Assignment 2: Exploring NLTK
[Here](Assignment2/Exploring_NLTK.ipynb) is a notebook guiding how I explored the Python 3 NLTK library, there is also a [pdf](Assignment2/Exploring_NLTK.pdf). I used text1 of the book library (Moby Dick by Herman Melville 1851), to print tokens, concordance, and compare NLTK count and list count modules. I also used some raw text of my own choosing to tokenize by words and sentences, as well as stem and lematize the text to compare results. This helped me familiarize with popular NLTK modules and how to utilize them for data processing.

## Assignment 3: Word Guessing Game

It is coded in [python](Assignment3/word_guessing_game.py) with the [data](Assignment3/data/anat19.txt)

### REQUIRED PARAMETERS:
    You must have a folder in the same directory named 'data' containing the
    text data file named 'anat19.txt' it can be found above with the 'data' link.

    or here as this github in Assignment 3:

    https://gihub.com/BridgetteBXP13/CS-4395.001---Human-Language-Techologies
Without the directory/file above the program will simply display an error message
telling you that your are missing the parameters and quit.

### Purpose:

This program was designed to practice data processing from a text file, creating tokens, lemmatizing, getting unique
lemmas, making a dictionary of lemmas by count, calculate lexical diversity, and creating a list of nouns from the
tagged nouns. After preprocessing text it will create a list of top 50 nouns and use them for the guessing game. The guessing game rules and displayed below

> #### Rules/How To Play:
> 
>    1. You will be given a word (each letter designated by an underscore
>    2. You will start off with 5 points, to keep playing you must keep your score above 0!
>    3. If you guess a correct letter, you will gain 1 point, and the letters will be revealed.
>    4. If you guess a correct letter you have already guessed, you will lose 2 points!
>    5. If you guess an incorrect letter you haven't guessed before, you will lose 1 point!
>    6. If you guess an incorrect letter you have already guessed, you will lose 3 points!
>    7. If you want to quit, enter '!' as a letter.
>    8. Try to see how long you last and how many words you can guess!

The game will operate with the rules/how to play above, if the user guesses all the words it will congratulate them.
Or it they quit it will output the ending score, number of words guessed, and the words guessed to the user. It will
also thank the user for playing.



### Functions:

#### readdatafile:
    This function reads in the parameter data file from the file directory, works with different OS systems. It is
    utilized by main to read the program's given parameters.

#### printnumtags:
    This function takes a list of tags and a number, it will print the first num of tags in the list. It is utilized by
    processrawtext to print 20 tags.

#### processrawtext:
    This function processes our raw text into text_tokens and unique noun lemmas and returns them.
    It is utilized by main to process the input from the anat19.txt file.

#### chooseword:
    This function takes a list of nouns, and randomly chooses a noun. Then removes such noun from the list.
     After it returns the chosen noun and the updated noun list. It is utilized by guessinggame.

#### guessinggame:
    This function runs the guessing game part of this program. It requires a list of nouns. First it will print
    rules and how to play to the user. Then it will continue to give the user words to guess (designated by
    underscores). The user will be prompted to guess a letter, if not given a letter it will continue to ask them to
    guess again. If the user inputs a letter it will assign appropriate letters to the word and add/subtract the
    appropriate amount of points according to the rules/how to play. If the user manages to guess all the words the
    game ends and the user will be congratulated as a guessing master. If the user quits by entering a '!' the function
    will print the end sequence and thank them for playing. The end sequence for both is displaying the ending number of
    points, number of guessed words, and the guessed words. The program will then return to main.
#### main:
    Verifies that the parameter data file anat19.txt is present (using readdatafile). Then it will use the
    processrawdata function to process the given raw text. Then it will calculate/print the lexical diversity of
    the return tokens/lemmas from processrawdata. After it will create a dictionary of the unique lemmas and sort them
    by their count. Next it prints and saves the first 50 nouns to a list. Finally it calls the guessinggame function to
    start the game with the given list of nouns.


## Assignment 4: WordNet
I created a [notebook](Assignment4/WordNet.ipynb) guiding how I utilized the Python 3 NLTK WordNet library and also output it as a [pdf](Assignment4/WordNet.pdf). I made use of synsets for both nouns and verbs, by extracting definitions, examples, lemmas, and traversing hierarchy. I also outputted their hypernyms, hyponyms, meronyms, holonyms, and antonyms. Using Morphy I attempted to make as many possible forms of the word 'walk'. Then I used the path_simularity, Wu-Palmer Simularity, and ran the Lesk algorithm for the words 'turtle' and 'snake'. I found that the Lesk algorithm really struggled with these words and I think it is because they are very context dependent. Then I utilized SentiWordNet to judge emotionally charged words and sentences. By using 'hate', 'love', and 'passionate' I mixed them in the sentences to see the results. Calculating the polarity scores for both each word in the sentence as well as the sum polarity of the sentence using a couple simple functions I wrote. Then I looked at collocation of text4 from NLTK.book and calculated the mutual information, which was high as exspected for the collocation I chose (Indian tribes).