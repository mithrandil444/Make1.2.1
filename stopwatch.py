#!/usr/bin/env python
"""
This is a python script for a stopwatch.
bron : https://www.includehelp.com/python/create-a-stopwatch-using-python.aspx
"""

# IMPORTS
import time

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O
print("Press Enter to start the stopwatch")     # Gives you instructions to start the stopwatch
print("and, press Enter to stop the stopwatch") # Gives you instructions to stop the stopwatch

def main():
    input("Press Enter to start the timer")     # Input for starting the stopwatch
    start_time = time.time()
    print("Stopwatch started...")               # Tells you that the stopwatch has started

    input("Press Enter to stop the timer")      # Input for stopping the stopwatch
    print("Stopwatch stopped...")               # Tells you that the stoptwatch has stopped
    end_time = time.time()

    print("The total time:", round(end_time - start_time, 2), "seconds")    # Tells you the amount of time has passed.

if __name__ == '__main__':  # code to execute if called from command-line
    main()
