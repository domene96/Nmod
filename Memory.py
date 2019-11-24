#!/usr/bin/env python

import sys

# Memory Structure for Nmod
class Memory:
    # Initialize memory
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
        self.slotsPerType = int((self.finalAddr - self.initAddr + 1) / 3)
        # Pointers
        self.intPointer = self.initAddr
        self.floatPointer = self.initAddr + self.slotsPerType
        self.charPointer = self.initAddr + self.slotsPerType * 2

    # Move to next address
    def nextMemoryDirection(self, type):
        if type == 'int':
            if self.intPointer > self.initAddr - 1 + self.slotsPerType:
                sys.exit("#MemoryManagement Error: int out of bounds " + str(self.intPointer) + " address")
            self.intPointer += 1
            return self.intPointer - 1
        elif type == 'float':
            if self.floatPointer > self.initAddr - 1 + self.slotsPerType * 2:
                sys.exit("#MemoryManagement Error: float out of bounds " + str(self.floatPointer) + " address")
            self.floatPointer += 1
            return self.floatPointer - 1
        elif type == 'char':
            if self.charPointer > self.initAddr - 1 + self.slotsPerType * 3:
                sys.exit("#MemoryManagement Error: char out of bounds " + str(self.charPointer) + " address")
            self.charPointer += 1
            return self.charPointer - 1

    # Get value from memory address
    def getValueAtAddress(self, addr):
        if addr >= self.initAddr:
            if addr <= self.initAddr + self.slotsPerType:
                return self.intMem[addr]
            elif addr <= self.initAddr + self.slotsPerType * 2:
                return self.floatMem[addr]
            elif addr <= self.initAddr + self.slotsPerType * 3:
                return self.charMem[addr]
            else:
                sys.exit("#MemoryManagement Error: upper out of bounds " + str(addr) + " address")
        else:
            sys.exit("#MemoryManagement Error: lower out of bounds " + str(addr) + " address")

    # Set a value to a memory address
    def setValueAtAddress(self, addr, val):
        if addr >= self.initAddr:
            if addr <= self.initAddr + self.slotsPerType:
                self.intMem[addr] = val
            elif addr <= self.initAddr + self.slotsPerType * 2:
                self.floatMem[addr] = val
            elif addr <= self.initAddr + self.slotsPerType * 3:
                self.charMem[addr] = val
            else:
                sys.exit("#MemoryManagement Error: upper out of bounds " + str(addr) + " address")
        else:
            sys.exit("#MemoryManagement Error: lower out of bounds " + str(addr) + " address")

    # Reserve a memory space for dimensional variables
    def reserveMemoryAddresses(self, type, size):
        if type == 'int':
            if self.intPointer >= self.initAddr - 1 + self.slotsPerType:
                sys.exit("#MemoryManagement Error: int out of bounds " + str(self.intPointer) + " address")
            self.intPointer += size
            return self.intPointer - size
        elif type == 'float':
            if self.floatPointer >= self.initAddr - 1 + self.slotsPerType * 2:
                print("1#MemoryManagement Error: float out of bounds " + str(self.floatPointer) + " address")
                # sys.exit("1#MemoryManagement Error: float out of bounds " + str(self.floatPointer) + " address")
            self.floatPointer += size
            return self.floatPointer - size
        elif type == 'char':
            if self.charPointer >= self.initAddr - 1 + self.slotsPerType * 3:
                sys.exit("#MemoryManagement Error: char out of bounds " + str(self.charPointer) + " address")
            self.charPointer += size
            return self.charPointer - size

    # Free the current memory space
    def clearMemory(self):
        # Clear variables
        self.intMem = {}
        self.floatMem = {}
        self.charMem = {}
        # Reset pointers
        self.intPointer = self.initAddr
        self.floatPointer = self.initAddr + self.slotsPerType
        self.charPointer = self.initAddr + self.slotsPerType * 2

    # Print Memory
    def printMemory(self):
        print(self.name + " Memory")
        print("-----------------------------")
        print("Int: ")
        # Print Ints
        for key, value in self.intMem.items():
            print(key, value)
        # Print Floats
        print("Float: ")
        for key, value in self.floatMem.items():
            print(key, value)
        # Print Chars
        print("Char: ")
        for key, value in self.charMem.items():
            print(key, value)
        print("-----------------------------")

    # Destroy memory
    def destroy(self):
        del self
