#!/usr/bin/env python

# Memory Structure for Nmod
class Memory:
    def __init__(self, name, initAddr, finalAddr):
        # Global / Local / Constant
        self.name = name

        # Limits
        self.initAddr = initAddr
        self.finalAddr = finalAddr

        # Local variables
        self.intMem = {}
        self.floatMem = {}
        self.charMem = {}

        # Number of slots per data type
        self.slotsPerType = (finalAddr - initAddr + 1) / 3

        # Counter for each type of variable
        self.varCount = [0,0,0,0]

    # Move to next address
    def nextMemoryDirection(self):
        1

    # Set a value to a memory address
    def setValueAtAddress(self):
        1

    # Get a value from memory address
    def getValueAtAddress(self):
        1

    # Reserve a memory space
    # for array or matrix
    def reserveMemoryAddresses(self):
        1

    # Get the address of a constant value
    def getConstantAddress(self, value):
        1

    # Free the current memory space
    def clearMemory(self):
        # Clear variables
        self.intMem = {}
        self.floatMem = {}
        self.charMem = {}
        # Clear variable counters
        self.varCount = [0,0,0,0]

    # Print Memory
    def printMemory(self):
        print(self.name + " Memory")
        print("-----------------------------")
        print("Int: ")
        # Print Ints
        for key, value in self.intMem.iteritems():
            print(key, value)
        # Print Floats
        print("Float: ")
        for key, value in self.floatMem.iteritems():
            print(key, value)
        # Print Chars
        print("Char: ")
        for key, value in self.charMem.iteritems():
            print(key, value)
        print("-----------------------------")
