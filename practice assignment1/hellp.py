"""
hello.py
A simple program to fulfill the requirements of Practical Assessment 01.
Author: Lihua Lu
References:
    [1] Python Software Foundation, "PEP 8 – Style Guide for Python Code," Python.org, 2001. [Online]. Available: https://peps.python.org/pep-0008/. [Accessed: Oct. 26, 2024].
    [2] Python Software Foundation, "PEP 257 – Docstring Conventions," Python.org, 2001. [Online]. Available: https://peps.python.org/pep-0257/. [Accessed: Oct. 26, 2024].
"""

import sys

def main():
    """
    The main function of the program.
    Prints a greeting, the programming language version, and the author's name.
    """
    # Print the custom greeting
    print("Hello Tuna Fish!")

    # Print the programming language and its version
    print(f"Language: Python {sys.version}")

    # Print the author's name
    print("Author: Lihua Lu")

# Check if this script is being run directly
if __name__ == "__main__":
    main()