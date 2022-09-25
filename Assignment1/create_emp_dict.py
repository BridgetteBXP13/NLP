'''
Welcome to create_emp_dict.py! Created by Bridgette Bryant, NETID: BMB180001
Created for Assignment 1 of 4395.001 Human Language Technologies in order to familiarize myself with python,
including simple file/data processing.

REQUIRED PARAMETERS:    You must have a folder in the same directory
                        name 'data' containing a file named 'data.csv'
                        it can be found here under Homework1:
                        https://bridgettebxp13.github.io/CS-4395.001---Human-Language-Technologies/

                        or here at this github in Assignment:
                        https://github.com/BridgetteBXP13/CS-4395.001---Human-Language-Technologies/
Without the directory/file above the program will simply give you an error message telling you that
you are missing the parameters!

This program takes a data.csv file as described above in the form:
Last,First,Middle Initial,ID,Office phone
Smith,Smitty,S,WH1234,5557771212......

A list of employees with their primary information, it then processes the data file, creates Person object, and
inserts that person object into a dictionary based on their ID.

The Person class has the following arguments:
    Last    -- For person's last name
    First   -- For person's first name
    Mi      -- For person's middle initial
    ID      -- For person's ID
    Phone   -- For person's phone

    It only has one function: display(), which displays the Person's information

readdatafile:
    This function simply opens the parameter data file up from the file directory, works with multiple os systems!

getuserinput:
    This function simply gets input from the user and returns it

removeTitles:
    This function removes the 'Last,First,Middle Initial,ID,Office phone' from the data file

verifyName:
    This function clean and verifies that a valid alphabetic name was given and returns it

verifyMidLetter:
    This function clean and verifies that a valid alphabetic letter was given and returns it

verifyId:
    This function clean and verifies that a valid id in the form XX0000 was given, if not it
     will use the getuserinput function to get valid input recursively, attaining valid input and returns it

verifyPhnNum:
    This function clean and verifies that a valid phone number of 10 digits was given, if not it
     will use the getuserinput function to get valid input recursively, attaining valid input and returns it

processData:
    This function takes the input data from main and processes all of it utilizing the functions above. After the
    data is cleaned and validated, it then inserts people in the employee dictionary one at a time in order on the
    data file with their ID as the key. The dictionary doesn't allow duplicate IDs and will notify the user of the
    error when adding people to the dictionary, but will not ask for any input. It then returns the finished
    dictionary to main.

Main:
    Verifies that the parameter data file data.csv is present. Then continues to use the readdatafile to read the
    data in data.csv, call the processData function to process the data. Then it simply saves the returned
     dictionary in a pickle file, opens the pickle file and prints the dictionary to the user in the terminal.


'''

import sys      # to get the system parameter (data.csv)
import os       # used to get the os system for data.csv
import re       # Used for processing the data
import pickle   # Used for saving/reading the finished dictionary


# Classes
class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last    # Person's last name
        self.first = first  # Person's first name
        self.mi = mi        # Person's middle name
        self.id = id        # Person's id
        self.phone = phone  # Person's phone number

    def display(self):
        print('\nEmployee id:', self.id)  # Prints the employee id
        # prints the firstname, middle initial, and lastname of person
        print('\t' + '\t' + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t' + '\t' + self.phone)  # prints the phone number of person


def readdatafile(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    return text_in


def getuserinput(neededInputType, errorMsg):
        print(errorMsg)
        rawInput = input("Please input a valid " + neededInputType + ': ')
        # print("input: " + rawInput)
        return rawInput


def removeTitles(data):
    data.reverse() # Reverses the data
    # Remove the last 5 items
    for i in range(0, 5):
        data.pop(len(data)-1)
    data.reverse()  # Re-reverse the data (back the correct order)
    return data # Return the data without the titles


def verifyName(name): # Verifies a name is Capital Case and only alpabetical letters
    # Strips the name of any non-alpha characters
    name = re.sub(r'[^a-zA-Z]', '', name)
    # Verify that it is Capital Case and return it!
    # print(name.capitalize())
    return name.capitalize()


def verifyMidLetter(mid):
    # Strips the Middle Initial of any non-alpha characters
    mid = re.sub(r'[^a-zA-Z]', '', mid)
    # Verify that it is uppercase
    mid = mid.upper()
    # Verify that mid is not empty!
    if len(mid) < 1:
        mid = 'X'
    # Verify that we return only a single letter (the first one)
    # print(mid[0])
    return mid[0]


def verifyID(id):
    # Verifies that the id is of correct length
    if not len(id) == 6:
        # Attempt to get a correct input from the user and recall this function using given input
        return verifyID(getuserinput('ID', "Invalid ID Length: " + id + ",\n a valid ID should be in the form: XX0000"))
        # print("id in length: " + id)
    else:
        # print("length is valid!")
        # Verifies the first two characters are letters
        if not id[0:2].isalpha():
            # Attempt to get a correct input from the user and recall this function using given input
            return verifyID(getuserinput('ID', "Invalid ID Form: " + id + ",\n a valid ID should be in the form: XX0000"))
            # print("id in isalpha: " + id)
        else:
            # print("first 2 chars are valid!")
            # Verifies the last 4 characters are numbers
            if not id[2:6].isdigit():
                # Attempt to get a correct input from the user and recall this function using given input
                return verifyID(getuserinput('ID', "Invalid ID Form: " + id + ",\n a valid ID should be in the form: XX0000"))
                # print("id in isdigit: " + id)
            else:
                # print("form is 100% valid!")
                # Verify that the letters are uppercase and return the id!
                # print(id.upper())
                return id.upper()

def verifyPhnNum(num):
    # Strips the phone number of anything but digits
    num = re.sub('\D', '', num)
    if not len(num) == 10:
        # Attempt to get a correct input from the user and recall this function using given input
        return verifyPhnNum(getuserinput('Phone Number', "Invalid Phone Number: " + num + ", a valid Phone number should be in 9 digits long (excluding non-digit characters)"))
        # print("phone number in length: " + num)
    else:
        # print("length is valid!")
        # Adds appropriate dashes to the phone number
        num = num[0:3] + '-' + num[3:6] + '-' + num[6:]
        return num

    # if we get here something went terribly wrong!
    # print('00HELP')


def processData(rawData) :# Removes the titles from the data (in this case it is built around 5 titles)
    # Replace any newlines with a comma for splitting
    rawData = rawData.replace("\n", ',')
    # split the data into text variables by comma
    data = rawData.split(',')

    # Remove the titles from the data
    data = removeTitles(data)

    # For each data set.... (groups of 5):
    i = 0 # The Index
    personDict = {} # The Dictionary of People we will return to main
    while i < len(data):
        # print(i)
        # Verify the Last name is Capital and replace it with verified input using splicing
        data = data[:i] + [verifyName(data[i])] + data[i + 1:]
        i += 1
        # print(i)

        # Verify the First name is Capital  and replace it with verified input using splicing
        data = data[:i] + [verifyName(data[i])] + data[i + 1:]
        i += 1
        # print(i)

        # Verify the middle initial is a single uppercase letter
        data = data[:i] + [verifyMidLetter(data[i])] + data[i + 1:]
        i += 1
        # print(i)

        # Verify the id is the form XX000, if missing or invalid we must get input from user
        data = data[:i] + [verifyID(data[i])] + data[i + 1:]
        i += 1
        # print(i)

        # Verify the phone number is in the form 999-999-9999
        data = data[:i] + [verifyPhnNum(data[i])] + data[i + 1:]
        i += 1
        # print(data)
        #print(data[i-5] +" "+ data[i-4] +" "+ data[i-3] +" "+ data[i-2] +" "+ data[i-1])
        # Now that everything is validated, we can create the person with the given info!
        p = Person(data[i-5], data[i-4], data[i-3], data[i-2], data[i-1])

        # Verify that the Person doesn't have a duplicate id!
        if personDict.__contains__(p.id):
            print("Error adding: ")
            p.display()
            print("Employee above has duplicate key!\n")
        else: # Add to our dictionary
            personDict[data[i-2]] = p
    # Return dictionary to main
    return personDict


if __name__ == '__main__':

    # Verifying that the system parameter 'data/data.csv' is in place
    if len(sys.argv) < 2:   # If not, print error message and exit
        print('Please setup the parameter \'data/data.csv\'')
        print('Exiting...')
    else:   # If so, continue
        fp = sys.argv[1]
        fileData = readdatafile(fp) # Read the file using the readdatafile function

        emplDict = processData(fileData) # Process the data using the processData function, get the processed

        # Verify dictionary is not empty!
        if len(emplDict) < 1:
            print("Error: No employees in dictionary to display! Please check input data in data.csv is valid.")
        else:
            # Save the dictionary as a pickle file
            pickle.dump(emplDict, open('employeeList.p', 'wb'))
            # Read the pickle file
            empl = pickle.load(open('employeeList.p', 'rb'))
            # Display the Employees to the terminal
            print("\n\nEmployees list: ")
            for e in empl:
                empl[e].display()
