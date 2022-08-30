# CS-4395.001---Human-Language-Technologies
This is a github to store my Human Language Technology projects from my CS 4395.001 class.

## Overview of Natural Language Processing (NLP)
[Here](Overview%20of%20NLP.pdf) is a lovely pdf which shows a brief overview of NLP.

## Assignment 1: Text Processing with Python

[Here](/Homework1/Homework1_bmb180001.py) is the code and the [data](/Homework1/data/data.csv) (required for input).

This Program takes one input file data.csv in a given data folder. It then processes the data and
displays it in an organized employee list in the terminal, and also saves it as a dictionary in a
pickle file 'employeeList.p'. To use this program you simply need to create the following data file
in a /data directory as shown below and make sure it is set as a parameter in your IDE. Also, make
sure your data.csv file is in the appropriate format as shown below, from there you can run the 
program with the given inputs, add your own, and give the program input as it requests. Enjoy!

Created for Homework 1 of 4395.001 Human Language Technologies in order to familiarize myself with python,
including simple file/data processing.

REQUIRED PARAMETERS:    You must have a folder in the same directory
                        name 'data' containing a file named 'data.csv'
                        it can be found [here](https://bridgettebxp13.github.io/CS-4395.001---Human-Language-Technologies/) under Homework1, or [here](https://github.com/BridgetteBXP13/CS-4395.001---Human-Language-Technologies/) at this github in Homework1.
                        
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

## Hello World Program

This program simply says "Hello World" using Python 3. It was simply made to go here during
the creation of this portfolio as a test program.

Here is the [code](helloworld.py) and simple [documentation](helloworld.txt).
