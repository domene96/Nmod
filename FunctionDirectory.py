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

    # Method to check if variable is atomic (int, float, char)
    def isAtomic(self, var):
        if isinstance(var, int):
            return True
        if isinstance(var, float):
            return True
        if isinstance(var, char):
            return True
        return False

    # Method to check if function name exists in variable table
    def varExists(self, var):
        print(var)
        return var in self.varTable.keys()

    # Method to add a new entry to the variable table
    def addVariable(self, var, type, addr, value, size, dim):
        print(var, type, addr, value, size, dim)
        if self.varExists(var):
            # Variable exists in table
            print('Variable ' + var + ' is already defined.')
        else:
            # Add variable entry to table
            self.varTable[var] = [type, addr, value, size, dim]

    # Method to get the type of a given variable
    def getType(self, var):
        if var in self.varTable:
            return self.varTable[var][0]
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to set the type of a given variable
    def setType(self, var, type):
        if var in self.varTable:
            self.varTable[var][0] = type
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to get the address of a given variable
    def getAddress(self, var):
        if var in self.varTable:
            return self.varTable[var][1]
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to set the address of a given variable
    def setAddress(self, var, addr):
        if var in self.varTable:
            self.varTable[var][1] = addr
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to get the value of a given variable
    def getVarValue(self, var):
        if var in self.varTable:
            return self.varTable[var][2]
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to set the value of a given variable
    def setVarValue(self, var, value):
        if var in self.varTable:
            self.varTable[var][2] = value
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to get the total size of a given variable
    def getTotalSize(self, var):
        if var in self.varTable:
            return self.varTable[var][3]
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to set the total size of a given variable
    def setTotalSize(self, var, size):
        if var in self.varTable:
            self.varTable[var][3] = size
        else:
            print('Variable ' + var + ' is not defined.')

    # Method to get the dimension pointer of a given variable
    def getDimPointer(self, var):
        if self.isAtomic(var):
            if var in self.varTable:
                return self.varTable[var][4]
            else:
                print('Variable ' + var + ' is not defined.')
        else:
                print('Variable ' + var + ' is not multidimensional.')

    # Method to set the dimension pointer of a given variable
    def setDimPointer(self, var, dim):
        if self.isAtomic(var):
            if var in self.varTable:
                self.varTable[var][4] = dim
            else:
                print('Variable ' + var + ' is not defined.')
        else:
            print('Variable ' + var + ' is not multidimensional.')

    # Method to print the variable table
    def print(self, var):
        print("Variable Table")
        print("-----------------------------")
        for key , value in self.varTable.items():
            print(key,"=>",value)
        print("-----------------------------")

    # Method to destroy the variable table
    def destroy(self):
        del self

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

    # Method to check if function name exists in function directory
    def functionExists(self, func, type, params):
        print(func, type, params)
        return func in self.functionDirectory.keys()

    # Method to add a new entry to the function directory
    def addFunction(self, func, type, varTable, params, quadPlace, addr, size):
        print(func, type, varTable, params, quadPlace, addr, size)
        if self.functionExists(func, type, params):
            # Function exists in directory
            print('Function ' + func + ' is already defined.')
        else:
            # Add function entry to directory
            self.functionDirectory[func] = [type, varTable, params, quadPlace, addr, size]

    # Method to get the type of a given function
    def getType(self, func):
        if func in self.functionDirectory:
            return self.functionDirectory[func][0]
        else:
            print('Function ' + func + ' is not defined.')

    # Method to set the type of a given function
    def setType(self, func, type):
        if func in self.functionDirectory:
            self.functionDirectory[func][0] = type
        else:
            print('Function ' + func + ' is not defined.')

    # Method to get the variables of a given function
    def getVarTable(self, func):
        if func in self.functionDirectory:
            return self.functionDirectory[func][1]
        else:
            print('Function ' + func + ' is not defined.')

    # Method to set the variables of a given function
    def setVarTable(self, func, varTable):
        if func in self.functionDirectory:
            self.functionDirectory[func][1] = varTable
        else:
            print('Function ' + func + ' is not defined.')

    # Method to get the parameters of a given function
    def getParams(self, func):
        if func in self.functionDirectory:
            return self.functionDirectory[func][2]
        else:
            print('Function ' + func + ' is not defined.')

    # Method to set the variables of a given function
    def setParams(self, func, params):
        if func in self.functionDirectory:
            self.functionDirectory[func][2] = params
        else:
            print('Function ' + func + ' is not defined.')

    # Method to add a parameter to a given function
    def addParameter(self, func, param):
        if func in self.functionDirectory:
            self.functionDirectory[func][2].push(param)
        else:
            print('Function ' + func + ' is not defined.')

    # Method to get the position of the functions' quad placement
    def getQuadPlace(self, func):
        if func in self.functionDirectory:
            return self.functionDirectory[func][3]
        else:
            print('Function ' + func + ' is not defined.')

    # Method to set the position of the functions' quad placement
    def setQuadPlace(self, func, pos):
        if func in self.functionDirectory:
            self.functionDirectory[func][3] = pos
        else:
            print('Function ' + func + ' is not defined.')

    # Method to get the memory address of a given function
    def getAddress(self, func):
        if func in self.functionDirectory:
            return self.functionDirectory[func][4]
        else:
            print('Function ' + func + ' is not defined.')

    # Method to set the memory address of a given function
    def setAddress(self, func, addr):
        if func in self.functionDirectory:
            self.functionDirectory[func][4] = addr
        else:
            print('Function ' + func + ' is not defined.')

    # Method to get the stack required by a given function
    def getStackSize(self, func):
        if func in self.functionDirectory:
            return self.functionDirectory[func][5]
        else:
            print('Function ' + func + ' is not defined.')

    # Method to set the stack required by a given function
    def setStackSize(self, func, size):
        if func in self.functionDirectory:
            self.functionDirectory[func][5] = size
        else:
            print('Function ' + func + ' is not defined.')

    # Method to print the function directory
    def print(self):
        print("Function Directory")
        print("-----------------------------")
        for key , value in self.functionDirectory.items():
            print(key,"=>",value)
        print("-----------------------------")

    # Method to delete the function directory
    def destroy(self):
        del self

    # Method to test the function directory
    def test(self):
        self.print()
        self.addFunction("Test","test",{},[],-1,0,0)
        self.print()
