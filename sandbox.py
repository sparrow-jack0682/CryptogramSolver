# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.
# Leave in code under testing, comment out code if needed for later
# reference, or delete code that is no longer wanted.
# 6. COMPARE ORIGINAL ARRAY AND ORDERED ARRAY AND BUILD A DICTIONARY TO REMEMBER ORIGINAL ORDERING (SPK).

import numpy as np
import re


def cipher_acceptor():
    # The line below tells Python we're going to use the same
    # global variable called cipher and that we are not creating
    # a new function-specific one also called cipher
    global cipher
    # Get an input from the user
    cipher = input("Enter the cipher:\n")
    print(type(cipher))
    # Make sure the user does not want to not quitting, and quit if a cipher is not entered
    if not (cipher == 'X' or cipher == 'x' or cipher is None or cipher == ''):
        # Check if input follows RegEx for a typical cryptoquip
        if not re.search(r'^[a-zA-Z\s\D.,\-\'\"?!]+$', cipher):
            # If it does not follow RegEx inform the user and restart the function
            # and give the user an option to quit
            print('\nInvalid cryptogram. Please retry or hit X to quit.\n\n')
            cipher_acceptor()
        else:
            # If the RegEx is fine, replace double spaces with single spaces and remove trailing spaces
            cipher = re.sub(r'(\s\s+)', " ", cipher.rstrip())  # rstrip() removes trailing spaces
    else:
        # Be courteous
        quit("\nThank you for trying out this program.")

def main():
    # Call acceptor() to accept an input cipher
    cipher_acceptor()
    # DELETE THE LINE BELOW WHEN THE PROGRAM IS COMPLETE

csnvihicjlmvopakcs;kca


if __name__ == '__main__':
    main()