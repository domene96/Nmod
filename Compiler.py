#!/usr/bin/env python

import sys
from Structures import *
from Semantic import *
from Memory import *
from FunctionDirectory import *

# Compiler implementation
class Compiler:
    # Initialize Compiler
    def __init__(self):
        self.semantic = Semantic()
        self.globalMem = Memory("Global",1000,1999)
        self.localMem = Memory("Local",2000,3999)
        self.constMem = Memory("Constant",4000,4999)
        self.functionDirectory = FunctionDirectory()
        self.subDirectory = FunctionDirectory()
        self.quadList = []
        self.operatorStack = Stack()
        self.operandStack = Stack()
        self.typeStack = Stack()
        self.jumpStack = Stack()
        self.paramStack = Stack()
        self.dimStack = Stack()

    # DIRECTORIES
    def insertFunctionDirectory(self, name, type):
        self.functionDirectory.addFunction(name,type,0,0,30000,30000)

    # VARIABLES
    def storeVariable(self, id):
        1

    def getStoredVariables(self):
        1

    def declareVariables(self, list, type):
        1

    # MODULES
    def declareModule(self, name):
        1

    # PARAMETERS
    def storeParameter(self, value):
        1

    def validateParameters(self):
        1

    def raiseParamCounter(self):
        1

    # STACKS
    # inserts
    def insertStackOperator(self, operator):
        1

    def insertStackOperand(self, operand):
        1

    def insertStackType(self, type):
        1

    def insertStackJump(self, jump):
        1

    def insertStackParam(self, param):
        1

    def insertStackDim(self, dim):
        1

    # tops
    def topStackOperatorLogical(self):
        1

    def topStackOperatorComparative(self):
        1

    def topStackOperatorTerms(self):
        1

    def topStackOperatorFactors(self):
        1

    # pops
    def popStackOperator(self):
        1

    def popStackOperand(self):
        1

    def popStackJump(self):
        1

    def popStackType(self):
        1

    # EXPRESSIONS
    def validateExpression(self, expression):
        1

    def validateSubExp(self, subexp):
        1

    def validateExp(self, exp):
        1

    def validateTerm(self, term):
        1

    def validateFactor(self, factor):
        1

    # QUADRUPLES
    def generateAssignmentQuadruples(self, expression):
        1

    def generateGotoQuadruples(self, expression):
        1

    def generateGotoFQuadruples(self, expression):
        1

    def generateGotoVQuadruples(self, expression):
        1

    def generateQuads(self, expression):
        1
