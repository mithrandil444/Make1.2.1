#!/usr/bin/env python
"""
Met dit rekenmachine kan je optellen,aftrekken,vermenigvuldigen en delen door 2 getallen te kiezen
bron : https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# Variabelen die je definieert
Number_1 = int(input("Pick a number: "))       # Input, pick your first number
Number_2 = int(input("Pick another number: ")) # Input, it lets you pick a second number4

what = input('''What would you like to do?
+ for addition
- for subtraction
* for multiplication
/ for division
''')

def main():
    if what == "+":
        print(Number_1 + Number_2)

    elif what == '-':
        print(Number_1 - Number_2)

    elif what == '*':
        print(Number_1 * Number_2)

    elif what == '*':
        print(Number_1 / Number_2)

    else:
        print('this is not a valid number')


if __name__ == '__main__':  # code to execute if called from command-line
    main()
