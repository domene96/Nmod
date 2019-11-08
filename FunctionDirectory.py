#!/usr/bin/env python

# Variable Table implementation
class VariableTable:
    # Initialize Variable Table
    def __init__(self):
        self.varTable = {}
            # [var_name][i]
            # [0] = type
            # [1] = memory direction
            # [2] = value
            # [3] = total size
            # [4] = dimension pointer

    def addVariable(self, var):
        1

    def varExists(self, var):
        1

    def getType(self, var):
        1

    def getAddress(self, var):
        1

    def isAtomic(self, var):
        1

    def getVarValue(self, var):
        1

    def setVarValue(self, var, value):
        1

    def getVarTotalSize(self, var):
        1

    def setVarTotalSize(self, var, size):
        1

    def getVarDimPointer(self, var):
        1

    def setVarDimPointer(self, var, dim):
        1

    def print(self, var):
        1

    def destroy(self):
        1

# Function Directory implementation
class FunctionDirectory:
    # Initialize Function Directory
    def __init__(self):
        self.functionDirectory = {}
            # [function name][i]
            # [0] = return type
            # [1] = dictionary for var table
            # [2] = array for parameters expected
            # [3] = quad place
            # [4] = memory direction
            # [5] = size of procedure stack
        self.paramCounter = 0

    # Checks if function name exists in function table
    def functionExists(self, func, type, params):
        return func in self.functionDirectory.keys()

    # Method to add a new entry to the procedure directory
    def addFunction(self, func, type, params, quadPlace, memDir, size):
        if self.functionExists(func, type, params):
            # Function exists in directory
            print('Function ' + func + ' is already defined.')
        else:
            # Add function entry to directory
            self.functionDirectory[func] = [type, varTable, params, quadPlace, memDir, size]

    def getFunctionType(self, func):
        1

    def setFunctionType(self, func, type):
        1

    def getVarTable(self, func):
        1

    def setVarTable(self, func, varTable):
        1

    def getParams(self, func):
        1

    def setParams(self, func, params):
        1

    def addParameter(self, param):
        1

    def getQuadPlace(self, func):
        1

    def setQuadPlace(self, func, pos):
        1

    def getAddress(self, func):
        1

    def setAddress(self, func, pos):
        1

    def getStackSize(self, func):
        1

    def setStackSize(self, func, pos):
        1

    def print(self):
        1

    def destroy(self):
        1
