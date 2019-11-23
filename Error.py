#!/usr/bin/env python

import sys

# Error Structure for Nmod
class Error:
    # Initialize error
    def __init__(self, message, exit = False, print = True):
        self.msg = message # replace this
        self.bExit = exit
        self.bPrint = print

    # Get error message
    def getMessage(self):
        return self.msg

    # Set error message
    def setMessage(self, val):
        self.msg = val

    # Get Exit check
    def getExit(self, val):
        return self.bExit

    # Set Exit check
    def setExit(self, val):
        self.bExit = val

    # Get Print check
    def getPrint(self, val):
        return self.bPrint

    # Set Print check
    def setPrint(self, val):
        self.bPrint = val

    # Revise gravity of Error
    def revise(self):
        # Terminate program
        if self.bExit:
            sys.exit(self.msg)
        # Print message
        if self.bPrint:
            print(self.msg)
        self.clear()

    # Method to clean error object
    def clear(self):
        self.msg = ""
        self.bExit = False
        self.bPrint = False

    # Destroy error
    def destroy(self):
        del self
