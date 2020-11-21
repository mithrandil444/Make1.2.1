#!/usr/bin/env python
"""
This scripts will ask you in which year you were born en calculate how old you are
and in which year you will be 50 years old.
Bron : https://www.youtube.com/watch?v=7lg5BHLrw4E
"""

# IMPORTS
import datetime

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O
Age = int(input('Please enter the year you were born: '))  # Input that asks you for your birthyear
Year = datetime.datetime.now().year    # Finds the current year that is displayed on your laptop


def main():
    print('You are ', Year - Age, ' Years old')        # Print your current age
    print('You will be 50 in this year: ',Age + 50)    # Print the year were you will be 50 years old




if __name__ == '__main__':  # code to execute if called from command-line
    main()
