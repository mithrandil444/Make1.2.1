#!/usr/bin/env python
"""
Dit is een scriptje dat automatisch je rpi updates doet.
"""

# IMPORTS


__author__ = "Sven De Visscher "
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O


def main():

sudo apt update && apt upgrade -y


if __name__ == '__main__':  # code to execute if called from command-line
    main()
