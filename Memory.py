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
        self.slotsPerType = int((self.finalAddr - self.initAddr + 1) / 3)
        # Pointers
        self.intPointer = self.initAddr
        self.floatPointer = self.initAddr + self.slotsPerType
        self.charPointer = self.initAddr + self.slotsPerType * 2

    # Move to next address
    def nextMemoryDirection(self, type):
        if type == 'int':
            if self.intPointer > self.initAddr - 1 + self.slotsPerType:
                print("#MemoryManagement Error: int upper out of bounds ", addr, " address")
            self.intPointer += 1
            return self.intPointer - 1
        elif type == 'float':
            if self.floatPointer > self.initAddr - 1 + self.slotsPerType * 2:
                print("#MemoryManagement Error: float upper out of bounds ", addr, " address")
            self.floatPointer += 1
            return self.floatPointer - 1
        elif type == 'char':
            if self.charPointer > self.initAddr - 1 + self.slotsPerType * 3:
                print("#MemoryManagement Error: char upper out of bounds ", addr, " address")
            self.charPointer += 1
            return self.charPointer - 1

    # Get value from memory address
    def getValueAtAddress(self, addr):
        if addr > self.initAddr:
            if addr < self.initAddr + self.slotsPerType:
                return self.intMem[addr]
            elif addr < self.initAddr + self.slotsPerType * 2:
                return self.floatMem[addr]
            elif addr < self.initAddr + self.slotsPerType * 3:
                return self.charMem[addr]
            else:
                print("#MemoryManagement Error: upper out of bounds ", addr, " address")
        else:
            print("#MemoryManagement Error: lower out of bounds ", addr, " address")

    # Set a value to a memory address
    def setValueAtAddress(self, addr, val):
        if addr > self.initAddr:
            if addr < self.initAddr + self.slotsPerType:
                intMem[addr] = val
            elif addr < self.initAddr + self.slotsPerType * 2:
                floatMem[addr] = val
            elif addr < self.initAddr + self.slotsPerType * 3:
                charMem[addr] = val
            else:
                print("#MemoryManagement Error: upper out of bounds ", addr, " address")
        else:
            print("#MemoryManagement Error: lower out of bounds ", addr, " address")

    # Reserve a memory space for dimensional variables
    def reserveMemoryAddresses(self, type, size):
        if type == 'int':
            if self.intPointer > self.initAddr - 1 + self.slotsPerType:
                print("#MemoryManagement Error: int upper out of bounds ", addr, " address")
            self.intPointer += size
            return self.intPointer - size
        elif type == 'float':
            if self.floatPointer > self.initAddr - 1 + self.slotsPerType * 2:
                print("#MemoryManagement Error: float upper out of bounds ", addr, " address")
            self.floatPointer += size
            return self.floatPointer - size
        elif type == 'char':
            if self.charPointer > self.initAddr - 1 + self.slotsPerType * 3:
                print("#MemoryManagement Error: char upper out of bounds ", addr, " address")
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

    # Destroy memory
    def destroy(self):
        del self
