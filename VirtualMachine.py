#!/usr/bin/env python

import sys
from Error import *
from Structures import *
from Memory import *
from FunctionDirectory import *

# Virtual Machine implementation
class VirtualMachine:
    # Initialize virtual machine
    def __init__(self):
        # Errors
        self.error = Error("", False, False)
        # Instruction Pointer
        self.instructionPointer = 0
        self.quadruples = None
        # Structures for processing
        self.functionDirectory = FunctionDirectory() # Function Directory plus Global and Constant Memory
        self.localMemHandler = {} # Local memory
        # Debug flag
        self.debug = 3 # Not passed by compiler: 0 nothing, 1 print quad count, 2 print results, 3 print quad

    # Run virtual machine
    def run(self, quads):
        self.quadruples = quads
        while self.instructionPointer < len(self.quadruples):
            quad = self.quadruples[self.instructionPointer]
            op = quad.getOperator()
            if self.debug >= 1:
                print(self.instructionPointer)
                if self.debug >= 3:
                    quad.print()
            if op == 5:
                self.assignOperation(quad)
            elif op >= 6 and op <= 9:
                self.arithmeticOperation(quad)
            elif op >= 10 and op <= 16:
                self.logicOperation(quad)
            elif op == 17:
                self.gotofOperation(quad)
            elif op == 18:
                self.gotovOperation(quad)
            elif op == 19:
                self.gotoOperation(quad)
            elif op == 20:
                self.writeOperation(quad)
            elif op == 21:
                self.readOperation(quad)
            elif op == 22:
                self.returnOperation(quad)
            elif op == 23:
                self.reviseOperation(quad)
            elif op == 24:
                self.eraOperation(quad)
            elif op == 25:
                self.paramOperation(quad)
            elif op == 26:
                self.gosubOperation(quad)
            elif op == 27:
                self.endprocOperation(quad)
            elif op > 28:
                self.specialOperation(quad)
            else:
                sys.exit('#RUNTIME ERROR VirtualMachineExecution: invalid quadruple: ', quad.print())
            self.instructionPointer += 1

    # Method to get value from memory address
    def getValAtMem(self, addr):
        if addr >= 1000 and addr <= 9999:
            return self.functionDirectory.globalMem.getValueAtAddress(addr)
        elif addr >= 10000 and addr <= 29999:
            return self.functionDirectory.localMem.getValueAtAddress(addr)
        elif addr >= 30000 and addr <= 39999:
            return self.functionDirectory.constMem.getValueAtAddress(addr)
        elif addr == -1:
            return self.returnMem.pop()
        else:
            sys.exit("#RUNTIME ERROR MemoryManagement: out of bounds ", addr, " address")

    # Method to set value at memory address
    def setValAtMem(self, addr, val):
        if addr >= 1000 and addr <= 9999:
            self.functionDirectory.globalMem.setValueAtAddress(addr, val)
        elif addr >= 10000 and addr <= 29999:
            self.functionDirectory.localMem.setValueAtAddress(addr, val)
        elif addr >= 30000 and addr <= 39999:
            self.functionDirectory.constMem.setValueAtAddress(addr, val)
        elif addr == -1:
            self.returnMem.push(val)
        else:
            sys.exit("#RUNTIME ERROR MemoryManagement: out of bounds ", addr, " address")

    # Method to execute write operations
    def writeOperation(self, quad):
        valAddr = quad.getResult()
        res = str(self.getValAtMem(valAddr))
        if self.debug >= 2:
            print("print ", res)

    # Method to execute read operations
    def readOperation(self, quad):
        1
        # resAddr = quad.getResult()
        # input = input()
        # res = str(input)
        # self.setValAtMem(resAddr, res)

    # Method to execute assignment operations
    def assignOperation(self, quad):
        resAddr = quad.getResult()
        valAddr = quad.getLeftOperand()
        res = self.getValAtMem(valAddr)
        print(resAddr, valAddr, res)
        if res == None:
            sys.exit("#RUNTIME ERROR AssignOperation: cannot perform assignment operation")
        self.setValAtMem(resAddr, res)
        if self.debug >= 2:
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute arithmetic operations
    def arithmeticOperation(self, quad):
        leftAddr = quad.getLeftOperand()
        rightAddr = quad.getRightOperand()
        resAddr = quad.getResult()
        leftVal = self.getValAtMem(leftAddr)
        rightVal = self.getValAtMem(rightAddr)
        if leftVal == None or rightVal == None:
            sys.exit("#RUNTIME ERROR VariableAccess Error: cannot perform arithmetic operation")
        opAddr = quad.getOperator()
        if self.debug >= 2:
            print(opAddr, leftVal, rightVal, resAddr)
        if opAddr == 6:
            res = int(leftVal) + int(rightAddr)
            self.setValAtMem(resAddr, res)
        elif opAddr == 7:
            res = int(leftVal) - int(rightAddr)
            self.setValAtMem(resAddr, res)
        elif opAddr == 8:
            res = int(leftVal) * int(rightAddr)
            self.setValAtMem(resAddr, res)
        elif opAddr == 9:
            if leftVal == 0 or rightVal == 0:
                sys.exit("#RUNTIME ERROR VariableAccess: cannot perform division by 0")
            res = int(leftVal) / int(rightAddr)
            self.setValAtMem(resAddr, res)
        else:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform arithmetic operation")
        if self.debug >= 2:
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute logical operations
    def logicOperation(self, quad):
        leftAddr = quad.getLeftOperand()
        rightAddr = quad.getRightOperand()
        resAddr = quad.getResult()
        leftVal = self.getValAtMem(leftAddr)
        rightVal = self.getValAtMem(rightAddr)
        if leftVal == None or rightVal == None:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform logical operation")
        opAddr = quad.getOperator()
        if opAddr == 10:
            res = int(leftVal > rightVal)
            self.setValAtMem(resAddr, res)
        elif opAddr == 11:
            res = int(leftVal < rightVal)
            self.setValAtMem(resAddr, res)
        elif opAddr == 12:
            res = int(leftVal >= rightVal)
            self.setValAtMem(resAddr, res)
        elif opAddr == 13:
            res = int(leftVal <= rightVal)
            self.setValAtMem(resAddr, res)
        elif opAddr == 14:
            res = int(leftVal == rightVal)
            self.setValAtMem(resAddr, res)
        elif opAddr == 15:
            res = int(leftVal and rightVal)
            self.setValAtMem(resAddr, res)
        elif opAddr == 16:
            res = int(leftVal or rightVal)
            self.setValAtMem(resAddr, res)
        else:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform logical operation")
        if self.debug >= 2:
            print(opAddr, resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute goto operations
    def gotoOperation(self, quad):
        self.instructionPointer = quad.getResult() - 1

    # Method to execute gotoF operations
    def gotofOperation(self, quad):
        checkAddr = quad.getLeftOperand()
        check = self.getValAtMem(checkAddr)
        if check > 0:
            self.instructionPointer = quad.getResult() - 1

    # Method to execute gotoV operations
    def gotovOperation(self, quad):
        1 # gotoV is not used within Nmod

    # Method to verify exp is within dimension bounds
    def reviseOperation(self, quad):
        leftAddr = quad.getLeftOperand()
        rightAddr = quad.getRightOperand()
        resAddr = quad.getResult()
        leftVal = self.getValAtMem(leftAddr)
        rightVal = self.getValAtMem(rightAddr)
        resVal = self.getValAtMem(resAddr)
        if resVal >= leftVal and resVal <= rightVal:
            if self.debug >= 2:
                print('revise ', leftVal, rightVal, resVal, True)
            return True
        if self.debug >= 2:
            print('revise ', leftVal, rightVal, resVal, False)
        return False

    # Method to execute return operations
    def returnOperation(self, quad):
        resAddr = quad.getResult()
        res = self.getValAtMem(resAddr)
        self.setValAtMem(resAddr, res)
        if self.debug >= 2:
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute Expansion of Activation Record
    def eraOperation(self, quad):
        1
        # self.functionStack.push(quad.getResult())
        # tempEra = ActivationRecord(self.functionDirectory.localMem)
        # self.localMemHandler.push(tempEra)
        # newMem = Memory("Temporal", 80000, 85000)
        # newEra = ActivationRecord(newMem)
        # if self.debug >= 4:
        #     print("Prev ERA")
        #     tempEra.printMemory()

    # Method to execute parameter operations
    def paramOperation(self, quad):
        1

    # Method to execute gosub operations
    def gosubOperation(self, quad):
        1
        # func = quad.getLeftOperand()
        # self.instructionPointer = self.functionDirectory.getQuadPlace(func) - 1

    # Method to execute endproc operations
    def endprocOperation(self, quad):
        1

    # Method to execute special function operations
    def specialOperation(self, quad):
        1

    # Method to print VM info
    def print(self, quad):
        self.functionDirectory.globalMem.print('Global')
        self.functionDirectory.localMem.print('Local')
        self.functionDirectory.constMem.print('Constant')

    # Method to clean VM
    def clear(self, quad):
        self.functionDirectory.globalMem.clearMemory()
        self.functionDirectory.localMem.clearMemory()
        self.functionDirectory.constMem.clearMemory()
        self.instructionPointer = 0
        self.quadruples = None

    # Method to destroy VM
    def destroy(self, quad):
        del self
