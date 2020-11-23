#!/usr/bin/env python
"""
This python script will tell you how many characters there are in your word.
bron : https://www.programiz.com/python-programming/methods/built-in/len
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


def main():
    Random_word = input("Type you word here: ")     # Input that will ask you for a random word

    len(Random_word)                                # This wil count the amount of characters of your chosen word
    print("The amount of character of your chosen word is: ", (len(Random_word)))
    # this will print the amount of characters of your chosen word

if __name__ == '__main__':  # code to execute if called from command-line
    main()
