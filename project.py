__author__ = "Aadit Kapoor"
__version__ = "1.0.0"

# imports
import sys # For stderr
import error # Basic error functions
import time # sleep() function
import mean # Mean computing functions
import search # Search functions
import display # Basic display functions
import input # Basic parse functions
import storer # Storing the data functions


# Variables to store search item number
count = 0
words_not_found = 0


# Main data structure of the program
data = []


# Opening the 'Words.txt' file
try:
    word_list = open("Words.txt","r")
except IOError:
    error.file_error()
finally:
    print "Opening Operation done!"


# Basic modifications code
data = storer.store_data(word_list)
storer.remove_slashn(data)
storer.to_lower(data)

# Closing the file
word_list.close()


# Getting input from the user
word = raw_input("Enter an item to be searched (Type \'exit\' to exit) :  ")

input.checker(word)

display.init("Intializing check")

# Checking
if search.letter(word,data):
    display.show("PASS")
    
else:
    display.show("EVERYTHING FALIED")


    






