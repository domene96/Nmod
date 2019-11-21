#!/usr/bin/env python

from Structures import *
from Semantic import *
from Memory import *

# Virtual Machine implementation
class VirtualMachine:
    # Initialize virtual machine
    def __init__(self):
        self.globalMem = []
        self.localMem = []
        self.constMem = []
        self.quadruples = []
        self.instructionPointer = 0
        self.funcMemTable = {}
        self.tempMem = [] # ERA
        self.returnMem = [] # ERA
        self.gosubStack = Stack()

    #
    def run(self, quad):
        while len(self.quadruples):
            quad = self.quadruples[self.instructionPointer]
            op = quad[0]
            if op == 5:
                self.assignOperation()
            elif op >= 6 and op <= 9:
                self.arithmeticOperation()
            elif op >= 10 and op <= 16:
                self.logicOperation()
            elif op == 17 or op == 18 or op == 19:
                self.gotoOperation()
            elif op == 20:
                self.writeOperation()
            elif op == 21:
                self.readOperation()
            elif op == 22:
                self.returnOperation()
            elif op == 23:
                self.reviseOperation()
            elif op == 24:
                self.eraOperation()
            elif op == 25:
                self.paramOperation()
            elif op == 26:
                self.gosubOperation()
            elif op == 27:
                self.endprocOperation()
            elif op > 28:
                self.specialOperation()
            else:
                print('#Virtual Machine Execution Error: invalid quadruple: ', quad)
                sys.exit()
            self.quadruples = self.quadruples[self.instructionPointer+1]

    #
    def fillMem(self):
        1

    #
    def getValueAtMem(self, addr):
        1

    #
    def setValueAtMem(self, addr, val):
        1

    #
    def writeOperation(self, quad):
        1

    #
    def readOperation(self, quad):
        1

    #
    def assignOperation(self, quad):
        1

    #
    def arithmeticOperation(self, quad):
        1

    #
    def logicOperation(self, quad):
        1

    #
    def gotoOperation(self, quad):
        1


    #
    def reviseOperation(self, quad):
        1

    #
    def returnOperation(self, quad):
        1

    #
    def eraOperation(self, quad):
        1

    #
    def paramOperation(self, quad):
        1

    #
    def gosubOperation(self, quad):
        1

    #
    def endprocOperation(self, quad):
        1

    #
    def specialOperation(self, quad):
        1

    #
    def print(self, quad):
        1

    #
    def clear(self, quad):
        1

    #
    def destroy(self, quad):
        1
