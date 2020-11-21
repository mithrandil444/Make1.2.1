#!/usr/bin/env python
"""
This is a python script that sums up a list that is given
this will let you add some words into the existing list en show it to you
bron 1: https://www.programiz.com/python-programming/methods/built-in/list
bron 2 : https://stackoverflow.com/questions/11574195/how-to-merge-multiple-lists-into-one-list-in-python
"""
"""
ik heb het nog niet helemaal gevonden hoe je de nieuwe woorden helemaal in de lijst krijgt 
maar dit is alvast een poging
"""

# IMPORTS
import itertools

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"



def main():
    fruit = ["appelen", "peren", "bananen"]     # A list of fruit
    print(list(fruit))                          # This prints the list of fruit

    more_fruit = input("Type here some more fruit: ")   # Input for more words or in this case more fruit
    extra_fruit = itertools.chain([fruit, more_fruit])
    print(list(extra_fruit))                            # Prints the existing list with the added words or fruit

if __name__ == '__main__':  # code to execute if called from command-line
    main()
