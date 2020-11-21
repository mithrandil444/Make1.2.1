#!/usr/bin/env python
"""
Met dit rekenmachine kan je optellen,aftrekken,vermenigvuldigen en delen door 2 getallen te kiezen
bron 1: https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
bron 2 : https://www.programiz.com/python-programming/examples/calculator
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# Variabelen die je definieert
Getal_1 = int(input("Pick a number: "))        # Input, kies je eerste getal
Getal_2 = int(input("Pick another number: "))  # Input, kies je 2de getal

what = input('''What would you like to do?     # wat wil je doen?
optellen for addition
aftrekken for subtraction
vermenigvuldigen for multiplication
delen for division
''')


def main():
    if what == "optellen":
        print(Getal_1 + Getal_2)

    elif what == 'aftrekken':
        print(Getal_1 - Getal_2)

    elif what == 'vermenigvuldigen':
        print(Getal_1 * Getal_2)

    elif what == 'delen':
        print(Getal_1 / Getal_2)




if __name__ == '__main__':  # code to execute if called from command-line
    main()
