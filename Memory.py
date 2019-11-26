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
        self.intUpperLimit = self.initAddr + self.slotsPerType - 1
        self.floatPointer = self.initAddr + self.slotsPerType
        self.floatUpperLimit = self.initAddr + self.slotsPerType * 2 - 1
        self.charPointer = self.initAddr + self.slotsPerType * 2
        self.charUpperLimit = self.initAddr + self.slotsPerType * 3

    # Move to next address
    def nextMemoryDirection(self, type):
        if type == 'int':
            if self.intPointer > self.intUpperLimit:
                sys.exit("#MemoryManagement Error: int out of bounds " + str(self.intPointer) + " address")
            self.setValueAtAddress(self.intPointer, None)
            self.intPointer += 1
            return self.intPointer - 1
        elif type == 'float':
            if self.floatPointer > self.floatUpperLimit:
                sys.exit("#MemoryManagement Error: float out of bounds " + str(self.floatPointer) + " address")
            self.setValueAtAddress(self.floatPointer, None)
            self.floatPointer += 1
            return self.floatPointer - 1
        elif type == 'char':
            if self.charPointer > self.charUpperLimit:
                sys.exit("#MemoryManagement Error: char out of bounds " + str(self.charPointer) + " address")
            self.setValueAtAddress(self.charPointer, None)
            self.charPointer += 1
            return self.charPointer - 1

    # Get value from memory address
    def getValueAtAddress(self, addr):
        if addr >= self.initAddr:
            if addr <= self.intUpperLimit:
                return self.intMem[addr]
            elif addr <= self.floatUpperLimit:
                return self.floatMem[addr]
            elif addr <= self.charUpperLimit:
                return self.charMem[addr]
            else:
                sys.exit("#MemoryManagement Error: upper out of bounds " + str(addr) + " address")
        else:
            sys.exit("#MemoryManagement Error: lower out of bounds " + str(addr) + " address")

    # Set a value to a memory address
    def setValueAtAddress(self, addr, val):
        if addr >= self.initAddr:
            if addr <= self.intUpperLimit:
                self.intMem[addr] = val
            elif addr <= self.floatUpperLimit:
                self.floatMem[addr] = val
            elif addr <= self.charUpperLimit:
                self.charMem[addr] = val
            else:
                sys.exit("#MemoryManagement Error: upper out of bounds " + str(addr) + " address")
        else:
            sys.exit("#MemoryManagement Error: lower out of bounds " + str(addr) + " address")

    # Reserve a memory space for dimensional variables
    def reserveMemoryAddresses(self, type, size):
        if type == 'int':
            if self.intPointer >= self.intUpperLimit:
                sys.exit("#MemoryManagement Error: int out of bounds " + str(self.intPointer) + " address")
            varSize = self.intPointer + size
            while self.intPointer < varSize:
                self.setValueAtAddress(self.intPointer, None)
                self.intPointer += 1
            return self.intPointer - size
        elif type == 'float':
            if self.floatPointer >= self.floatUpperLimit:
                sys.exit("#MemoryManagement Error: float out of bounds " + str(self.floatPointer) + " address")
            varSize = self.floatPointer + size
            while self.floatPointer < varSize:
                self.setValueAtAddress(self.floatPointer, None)
                self.floatPointer += 1
            return self.floatPointer - size
        elif type == 'char':
            if self.charPointer >= self.charUpperLimit:
                sys.exit("#MemoryManagement Error: char out of bounds " + str(self.charPointer) + " address")
            varSize = self.charPointer + size
            while self.charPointer < varSize:
                self.setValueAtAddress(self.charPointer, None)
                self.charPointer += 1
            return self.charPointer - size

    # Check to see if val exists in memory
    def findVal(self, val, type):
        if type == 'int':
            low = self.initAddr
            high = self.intPointer
            while low < high:
                if str(val) == str(self.getValueAtAddress(low)):
                    return low
                low += 1
            return False
        elif type == 'float':
            low = self.intUpperLimit + 1
            high = self.floatPointer
            while low < high:
                if str(val) == str(self.getValueAtAddress(low)):
                    return low
                low += 1
            return False
        elif type == 'char':
            low = self.floatUpperLimit + 1
            high = self.charPointer
            while low < high:
                if str(val) == str(self.getValueAtAddress(low)):
                    return low
                low += 1
            return False
        else:
            sys.exit("#MemoryManagement Error: out of bounds " + str(addr) + " address")

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
