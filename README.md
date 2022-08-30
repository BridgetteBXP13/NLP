# CS-4395.001---Human-Language-Technologies
This is a github to store my Human Language Technology projects from my CS 4395.001 class.

## Overview of Natural Language Processing (NLP)
[Here](Overview%20of%20NLP.pdf) is a lovely pdf which shows a brief overview of NLP.

## Assignment 1: Text Processing with Python

[Here](Homework1_bmb180001.py) is the code and the [data](data/data.csv) (required for input).

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
                        it can be found here under Homework1:
                        https://bridgettebxp13.github.io/CS-4395.001---Human-Language-Technologies/

                        or here at this github in Homework1:
                        https://github.com/BridgetteBXP13/CS-4395.001---Human-Language-Technologies/
Without the directory/file above the program will simply give you an error message telling you that
you are missing the parameters!

This program takes a data.csv file as described above in the form:
Last,First,Middle Initial,ID,Office phone
Smith,Smitty,S,WH1234,5557771212......

A list of employees with their primary information, it then processes the data file, creates Person object, and
inserts that person object into a dictionary based on their ID.

It gives the User opportunities to fix errors in employee IDs and Phone Numbers recursively. 


Here is the [code](helloworld.py) and simple [documentation](helloworld.txt).

## Hello World Program

This program simply says "Hello World" using Python 3. It was simply made to go here during
the creation of this portfolio as a test program.

Here is the [code](helloworld.py) and simple [documentation](helloworld.txt).
