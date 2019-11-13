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
        self.globalMem = Memory("Global", 1000, 9999)
        self.localMem = Memory("Local", 10000, 29999)
        self.constMem = Memory("Constant", 30000, 49999)
        self.functionDirectory = FunctionDirectory()
        self.subDirectory = FunctionDirectory()
        self.globals = VariableTable()
        self.localFunc = "" # function in question
        self.constants = VariableTable()
        self.quadList = []
        self.operandStack = Stack()
        self.operatorStack = Stack()
        self.typeStack = Stack()
        self.jumpStack = Stack()
        self.paramStack = Stack()
        self.dimStack = Stack()

    # PROCEDURES
    def insertFunctionDirectory(self, name, type):
        self.functionDirectory.addFunction(name, type, VariableTable(), VariableTable(), None, None, None)

    # CONSTANTS
    def insertConstant(self, type, id):
        1

    # VARIABLES
    def insertVarTable(self, func, id, type):
        1

    def getVarVal(self, func, id):
        1

    def getVarType(self, func, id):
        1

    def getVarAddr(self, func, id):
        1

    def getVarSize(self, func, id):
        1

    def getVarDim(self, func, id):
        1

    # DIMENSIONAL VARIABLES
    def initDimVar(self):
        1

    def setDimLowBound(self, i):
        1

    def setDimHighBound(self, i):
        1

    def addDimension(self):
        1

    def calculateK(self):
        1

    def associateBaseAddr(self):
        1

    def dimVarBegin(self):
        1

    def nextDimension(self):
        1

    def dimVarEnd(self):
        1

    # MAIN
    def mainBegin(self):
        1

    def mainEnd(self):
        1

    # MODULES
    def moduleBegin(self):
        1

    def moduleEnd(self):
        1

    def getModuleReturnAddr(self, func):
        1

    def getModuleReturnType(self, func):
        1

    # PARAMETERS
    def insertParamTable(self, func, id, type):
        1

    def moveParameterPointer(self):
        1

    def nullParameterPointer(self):
        1

    # Validate that the parameter types equal the expected parameter types of the function
    def validateParameters(self, func):
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

    # QUADRUPLES
    # Method to generate quadruples for factor, term, exp, sub_exp and expression
    def generateQuad(self, expression):
        1

    # Method to validate condition and generate quadruples
    def conditionStart(self):
        1

    # Method to fill remaining gotoF
    def conditionEnd(self):
        1

    # Method to utilize else condition (generate quadruples, including remaining goto)
    def conditionElse(self):
        1

    # Method to validate condition of cicle and generate quadruples, including remaining gotoF
    def cicleStart(self):
        1

    # Method to fill remaining goto
    def cicleEnd(self):
        1

    # Method to generate quadruples of an assignment
    def generateAssignmentQuadruples(self, expression):
        1

    def generateGotoQuadruples(self, expression):
        1

    def generateGotoFQuadruples(self, expression):
        1

    def generateGotoVQuadruples(self, expression):
        1

    def generateERA(self):
        1

    def generateActionParameter(self):
        1

    def generateGoSub(self):
        1

    def fillGoto():
        1

    def fillGotoF():
        1

    def fillGotoV():
        1

    # STACKS
    # false bottom
    def insertFalseBottom(self):
        self.operatorStack.push('(')

    def removeFalseBottom(self):
        if self.operatorStack.top() == '(':
            self.operatorStack.pop()
        else:
            print("Error")

    # inserts
    def insertStackOperator(self, operator):
        self.operatorStack.push(operator)

    def insertStackOperand(self, operand):
        self.operandStack.push(operand)

    def insertStackType(self, type):
        self.typeStack.push(type)

    def insertStackJump(self, jump):
        self.jumpStack.push(jump)

    def insertStackParam(self, param):
        self.paramStack.push(param)

    def insertStackDim(self, dim):
        self.dimStack.push(dim)

    # tops
    def topStackOperator(self):
        return self.operatorStack.top()

    def topStackOperand(self):
        return self.operandStack.top()

    def topStackType(self):
        return self.typeStack.top()

    def topStackJump(self):
        return self.jumpStack.top()

    def topStackParam(self):
        return self.paramStack.top()

    def topStackDim(self):
        return self.dimStack.top()

    # Check if tops are certain operator
    def topStackOperatorLogical(self):
        top = self.operatorStack.top()
        if top == 'and' or top == 'or':
            return True
        return False

    def topStackOperatorComparative(self):
        top = self.operatorStack.top()
        if top == '<=' or top == '>=' or top == 'equal' or top == '<' or top == '>':
            return True
        return False

    def topStackOperatorTerms(self):
        top = self.operatorStack.top()
        if top == '+' or top == '-':
            return True
        return False

    def topStackOperatorFactors(self):
        top = self.operatorStack.top()
        if top == '*' or top == '/':
            return True
        return False

    # pops
    def popStackOperator(self):
        self.operatorStack.pop()

    def popStackOperand(self):
        self.operandStack.pop()

    def popStackType(self):
        self.typeStack.pop()

    def popStackJump(self):
        self.jumpStack.pop()

    def popStackParam(self):
        self.paramStack.pop()

    def popStackDim(self):
        self.dimStack.pop()
