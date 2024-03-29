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
        self.functionDirectory = FunctionDirectory() # Function Directory including Global and Constant Memory
        self.localMemHandler = {} # Local memories
        self.functionStack = Stack() # Local function stack
        self.memStack = Stack() # ERA stack
        self.jumpStack = Stack() # Jump stack
        self.paramCount = 0
        # Debug flag
        self.debug = 0 # Not passed by compiler: 0 running VM, 1 current issues, 2 quad count, 3 current quad, 4 resolved issues

    # Method to check if current local function is recursive
    def checkRecursive(self):
        if self.functionStack.top() != 'global':
            if self.functionDirectory.getVarTable('global').varExists(self.functionStack.top()):
                return True
        return False

    # Methods to handle memory directions which store memory directions
    def checkVariables(self, leftAddr, rightAddr, resAddr):
        if isinstance(leftAddr, str):
            if leftAddr[0] == '(':
                leftAddr = leftAddr[1:-1]
                leftVal = int(leftAddr) # Set memory direction as value
            if leftAddr[0] == '¿':
                leftAddr = int(leftAddr[1:])
                leftAddr = int(self.getValAtMem(leftAddr)) # Get memory direction at memory direction
                leftVal = self.getValAtMem(leftAddr) # Set memory direction as value
        if isinstance(rightAddr, str):
            if rightAddr[0] == '(':
                rightAddr = rightAddr[1:-1]
                rightVal = int(rightAddr) # Set memory direction as value
            if rightAddr[0] == '¿':
                rightAddr = int(rightAddr[1:])
                rightAddr = int(self.getValAtMem(rightAddr)) # Get memory direction at memory direction
                rightVal = self.getValAtMem(rightAddr) # Set memory direction as value
        if isinstance(resAddr, str):
            if resAddr[0] == '(':
                resAddr = int(resAddr[1:-1]) # Set memory direction as value
            if resAddr[0] == '¿':
                resAddr = int(resAddr[1:])
        if not isinstance(leftAddr, str):
            leftVal = self.getValAtMem(leftAddr)
        if not isinstance(rightAddr, str):
            rightVal = self.getValAtMem(rightAddr)
        return leftVal, rightVal, resAddr

    # Methods to handle memory directions which store memory directions
    def checkVariable(self, resAddr, depth):
        if isinstance(resAddr, str):
            if resAddr[0] == '(':
                resAddr = resAddr[1:-1]
                res = int(resAddr) # Set memory direction as value
            if resAddr[0] == '¿':
                resAddr = int(resAddr[1:])
                resAddr = int(self.getValAtMem(resAddr)) # Get memory direction at memory direction
                if depth == 'val':
                    res = self.getValAtMem(resAddr) # Set memory direction as value
            if depth == 'val':
                return res
            else:
                return resAddr
        if depth == 'val':
            res = str(self.getValAtMem(resAddr))
            return res
        else:
            return resAddr

    # Run virtual machine
    def run(self, quads):
        print("Virtual Machine Running --- --- --- ---")
        self.quadruples = quads
        self.functionStack.push('global')
        while self.instructionPointer < len(self.quadruples):
            quad = self.quadruples[self.instructionPointer]
            op = quad.getOperator()
            if self.debug >= 2:
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
                self.endOperation(quad)
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
            elif op == 28:
                self.returnOperation(quad)
            elif op > 28:
                self.specialOperation(quad)
            else:
                sys.exit('#RUNTIME ERROR VirtualMachineExecution: invalid quadruple: ' + str(quad.print()))
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
            sys.exit("#RUNTIME ERROR MemoryManagement: out of bounds " + str(addr) + " address")

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
            sys.exit("#RUNTIME ERROR MemoryManagement: out of bounds " + str(addr) + " address")

    # Method to execute write operations
    def writeOperation(self, quad):
        resAddr = quad.getResult()
        res = self.checkVariable(resAddr, 'val')
        if self.debug >= 0:
            print("printing ", res)

    # Method to execute read operations
    def readOperation(self, quad):
        resAddr = quad.getResult()
        res = self.getValAtMem(resAddr)
        res = res[1:-1]
        try:
            file = open(res, 'r')
            if file.mode == 'r':
                content = file.read()
                if self.debug >= 0:
                    print("reading ", content)
        except:
            sys.exit("#RUNTIME ERROR FileManipulation: file " + str(res) + " does not exist")

    # Method to execute assignment operations
    def assignOperation(self, quad):
        resAddr = quad.getResult()
        valAddr = quad.getLeftOperand()
        val = self.checkVariable(valAddr, 'val')
        resAddr = self.checkVariable(resAddr, 'mem')
        if val == None:
            sys.exit("#RUNTIME ERROR AssignOperation: cannot perform assignment operation")
        self.setValAtMem(resAddr, val)
        if self.debug >= 1:
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute arithmetic operations
    def arithmeticOperation(self, quad):
        leftAddr = quad.getLeftOperand()
        rightAddr = quad.getRightOperand()
        resAddr = quad.getResult()
        leftVal, rightVal, resAddr = self.checkVariables(leftAddr, rightAddr, resAddr)
        if leftVal == None or rightVal == None:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform arithmetic operation unassigned variable")
        opAddr = quad.getOperator()
        if self.debug >= 1:
            print(opAddr, leftVal, rightVal, resAddr)
        if opAddr == 6:
            res = float(leftVal) + float(rightVal)
            if self.debug >= 1:
                print(float(leftVal) + float(rightVal))
        elif opAddr == 7:
            res = float(leftVal) - float(rightVal)
            if self.debug >= 1:
                print(float(leftVal) - float(rightVal))
        elif opAddr == 8:
            res = float(leftVal) * float(rightVal)
            if self.debug >= 1:
                print(float(leftVal) * float(rightVal))
        elif opAddr == 9:
            if leftVal == 0 or rightVal == 0:
                sys.exit("#RUNTIME ERROR VariableAccess: cannot perform division by 0")
            res = float(leftVal) / float(rightVal)
            if self.debug >= 1:
                print(float(leftVal) / float(rightVal))
        else:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform arithmetic operation operator not found")
        self.setValAtMem(resAddr, res)
        if self.debug >= 1:
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute logical operations
    def logicOperation(self, quad):
        leftAddr = quad.getLeftOperand()
        rightAddr = quad.getRightOperand()
        resAddr = quad.getResult()
        leftVal = self.checkVariable(leftAddr, 'val')
        rightVal = self.checkVariable(rightAddr, 'val')
        if leftVal == None or rightVal == None:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform logical operation")
        opAddr = quad.getOperator()
        if opAddr == 10:
            if self.debug >= 4:
                print("logic > ", float(leftVal), float(rightVal), int((float(leftVal) > float(rightVal)) == True))
            res = int((float(leftVal) > float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        elif opAddr == 11:
            if self.debug >= 4:
                print("logic < ", float(leftVal), float(rightVal), int((float(leftVal) < float(rightVal)) == True))
            res = int((float(leftVal) < float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        elif opAddr == 12:
            if self.debug >= 4:
                print("logic >= ", float(leftVal), float(rightVal), int((float(leftVal) >= float(rightVal)) == True))
            res = int((float(leftVal) >= float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        elif opAddr == 13:
            if self.debug >= 4:
                print("logic <= ", float(leftVal), float(rightVal), int((float(leftVal) <= float(rightVal)) == True))
            res = int((float(leftVal) <= float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        elif opAddr == 14:
            if self.debug >= 4:
                print("logic == ", float(leftVal), float(rightVal), int((float(leftVal) == float(rightVal)) == True))
            res = int((float(leftVal) == float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        elif opAddr == 15:
            if self.debug >= 4:
                print("logic and ", float(leftVal), float(rightVal), int((float(leftVal) and float(rightVal)) == True))
            res = int((float(leftVal) and float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        elif opAddr == 16:
            if self.debug >= 4:
                print("logic and ", float(leftVal), float(rightVal), int((float(leftVal) or float(rightVal)) == True))
            res = int((float(leftVal) or float(rightVal)) == True)
            self.setValAtMem(resAddr, res)
        else:
            sys.exit("#RUNTIME ERROR VariableAccess: cannot perform logical operation")
        if self.debug >= 4:
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute goto operations
    def gotoOperation(self, quad):
        self.instructionPointer = quad.getResult() - 1
        if self.debug >= 4:
            print("moved to ", self.instructionPointer + 1)

    # Method to execute gotoF operations
    def gotofOperation(self, quad):
        checkAddr = int(quad.getLeftOperand())
        if checkAddr == 0:
            check = 0
        elif checkAddr == 1:
            check = 1
        else:
            check = self.getValAtMem(checkAddr)
        if check > 1 or check == 0:
            self.instructionPointer = quad.getResult() - 1
            if self.debug >= 4:
                print("moved to ", self.instructionPointer + 1)

    # Method to execute gotoV operations
    def gotovOperation(self, quad):
        1 # gotoV is not used within Nmod

    # Method to verify exp is within dimension bounds
    def reviseOperation(self, quad):
        leftAddr = quad.getLeftOperand()
        rightAddr = quad.getRightOperand()
        resAddr = quad.getResult()
        leftVal = float(self.getValAtMem(leftAddr))
        rightVal = float(self.getValAtMem(rightAddr))
        resVal = float(self.getValAtMem(resAddr))
        if resVal >= leftVal and resVal <= rightVal:
            if self.debug >= 4:
                print('revise ', leftVal, rightVal, resVal, True)
            return True
        if self.debug >= 4:
            print('revise ', leftVal, rightVal, resVal, False)
        return False

    # Method to execute Expansion of Activation Record
    def eraOperation(self, quad):
        self.functionStack.push(quad.getResult())
        localEra = ActivationRecord(self.functionDirectory.localMem)
        self.memStack.push(localEra)
        newMem = Memory("ERA", 10000, 29999)
        newEra = ActivationRecord(newMem)
        self.memStack.push(newEra)
        if self.debug >= 1:
            localEra.printMemory()
            newEra.printMemory()
        if self.debug >= 1:
            print("ERA for ", self.functionStack.top(), " created")

    # Method to execute parameter operations
    def paramOperation(self, quad):
        paramAddr = quad.getLeftOperand()
        paramVal = self.checkVariable(paramAddr, 'val')
        if self.debug >= 4:
            print('param', self.paramCount, paramAddr, paramVal)
        funcParamAddr = self.functionDirectory.getVarTable(self.functionStack.top()).paramMemAddr(self.paramCount)
        localEra = self.memStack.top()
        localEra.eraMem.setValueAtAddress(funcParamAddr, paramVal)
        self.paramCount += 1

    # Method to execute gosub operations
    def gosubOperation(self, quad):
        self.paramCount = 0
        newEra = self.memStack.top()
        if self.debug >= 1:
            self.functionStack.print()
            newEra.printMemory()
        self.functionDirectory.localMem = newEra.eraMem
        self.jumpStack.push(self.instructionPointer)
        jump = quad.getResult()
        if self.debug >= 4:
            print("moved to ", jump)
        self.instructionPointer = int(jump) - 1

    # Method to execute endproc operations
    def endprocOperation(self, quad):
        self.memStack.pop()
        self.instructionPointer = self.jumpStack.pop()
        if self.debug >= 4:
            print("moved to ", self.instructionPointer)

    # Method to execute return operations
    def returnOperation(self, quad):
        self.functionStack.pop()
        endEra = self.memStack.pop()
        nextEra = self.memStack.pop()
        self.instructionPointer = self.jumpStack.pop()
        if self.debug >= 1:
            print("moved to ", self.instructionPointer + 1)
            endEra.printMemory()
            nextEra.printMemory()
        if self.debug >= 4:
            self.functionStack.print()
            self.memStack.print()
        if self.checkRecursive():
            self.functionDirectory.localMem = nextEra.eraMem
        else:
            self.functionDirectory.localMem = endEra.eraMem
        valAddr = quad.getLeftOperand()
        resAddr = quad.getResult()
        val = self.getValAtMem(valAddr)
        self.setValAtMem(resAddr, val)
        if self.debug >= 1:
            print('return to ', resAddr, ' => ', val)
            print(resAddr, " = ", self.getValAtMem(resAddr))

    # Method to execute special function operations
    def specialOperation(self, quad):
        print("Special operation " + str(quad.getOperator()) + " is not available yet, try again later.")

    # Method to end program
    def endOperation(self, quad):
        sys.exit("Goodbye :)")

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
