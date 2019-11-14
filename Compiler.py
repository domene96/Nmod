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
        # Semantics
        self.semantic = Semantic()
        # Memory
        self.globalMem = Memory("Global", 1000, 9999)
        self.localMem = Memory("Local", 10000, 29999)
        self.constMem = Memory("Constant", 30000, 39999)
        # Procedures
        self.functionDirectory = FunctionDirectory()
        self.subDirectory = FunctionDirectory()
        # Variables
        self.globals = VariableTable()
        self.localFunc = ''
        self.localType = ''
        self.constants = {}
        # Quadruples
        self.quadList = []
        self.quadCount = 0
        self.paramCount = 1
        self.operandStack = Stack()
        self.operatorStack = Stack()
        self.typeStack = Stack()
        self.jumpStack = Stack()
        self.dimStack = Stack()

    # PROCEDURES
    def insertFunctionDirectory(self, func, type):
        quad = Quadruple(self.semantic.operatorToKey['goto'], None, None, None)
        self.quadList.append(quad)
        self.quadCount += 1
        self.jumpStack.push(self.quadCount-1)
        if self.functionDirectory.addFunction(func, type, VariableTable(), [], None, None, None):
            return True
        else:
            print("#FunctionDeclaration Error: The function ", func, " was not declared properly")
            return False

    # CONSTANTS
    def insertConstant(self, type, val):
        if val not in self.constants:
            self.constants[val] = [self.constMem.nextMemoryDirection(type), val]
            return self.constants[val][0]
        #else:
            #print("#ConstantDeclaration Info: The constant ",val," exists")

    # VARIABLES
    def insertVarTable(self, func, id, type):
        #print(func, id, type)
        if self.functionDirectory.functionExists(func):
            if func == 'global':
                memDir = self.globalMem.nextMemoryDirection(type)
            else:
                memDir = self.localMem.nextMemoryDirection(type)
            self.functionDirectory.getVarTable(func).addVariable(id, type, memDir, None, None, None)
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    def getVarVal(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getValue(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getValue(id)
            else:
                print("#VariableDeclaration Error: The variable ",id," is not defined")
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")

    def getVarType(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                self.localType = self.functionDirectory.getVarTable(func).getType(id)
                return self.localType
            elif self.functionDirectory.getVarTable('global').varExists(id):
                self.localType = self.functionDirectory.getVarTable('global').getType(id)
                return self.localType
            else:
                print("#VariableDeclaration Error: The variable ",id," is not defined")
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")

    def getVarAddr(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getAddress(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getAddress(id)
            else:
                print("#VariableDeclaration Error: The variable ",id," is not defined")
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")

    def getVarSize(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getTotalSize(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getTotalSize(id)
            else:
                print("#VariableDeclaration Error: The variable ",id," is not defined")
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")

    def getVarDim(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getVDimPointer(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getVDimPointer(id)
            else:
                print("#VariableDeclaration Error: The variable ",id," is not defined")
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")

    # DIMENSIONAL VARIABLES
    def initDimVar(self):
        id = self.operandStack.pop()
        type = self.typeStack.pop()
        self.dimStack.push({id, type})

    def setDimLowBound(self, val):
        1

    def setDimHighBound(self, val):
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
        self.localMem.clearMemory()

    def mainEnd(self):
        #self.functionDirectory.print()
        self.printQuadruples();

    # MODULES
    def moduleBegin(self):
        self.localMem.clearMemory()

    def moduleEnd(self):
        1

    def getModuleReturnAddr(self, func):
        1

    def getModuleReturnType(self, func):
        1

    # PARAMETERS
    def insertParam(self, func, id, type):
        if self.functionDirectory.functionExists(func):
            if id not in self.functionDirectory.getParams(func):
                self.functionDirectory.getParams(func).append(type)
            else:
                print("#ParameterDeclaration Error: The parameter ",id," exists")
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")

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

    # MEMORY
    # Get memory address of id
    def getMemAddr(self, id):
        if self.functionDirectory.getVarTable(self.localFunc).varExists(id):
            return self.functionDirectory.getVarTable(self.localFunc).getAddress(id)
        elif self.functionDirectory.getVarTable('global').varExists(id):
            return self.functionDirectory.getVarTable('global').getAddress(id)
        elif id in self.constants:
            return self.constants[id][0]
        else:
            print("#MemoryManagement Error: Attempting to find ",id," was not found")

    # Temporal address to store quad result
    def getTempAddr(self, type):
        return self.localMem.nextMemoryDirection(type)

    # QUADRUPLES
    # Print quadList
    def printQuadruples(self):
        for quad in self.quadList:
            quad.print()

    # General check for linear expressions (step #4 condition)
    def checkLevelToOp(self, level):
        operator = self.operatorStack.top()
        if (level == 'term' and (operator == '+' or operator == '-')) or (level == 'factor' and (operator == '*' or operator == '/')) or (level == 'exp' and (operator == 'equal' or operator == '>=' or operator == '<=' or operator == '>' or operator == '<')) or (level == 'sub_exp' and (operator == 'and' or operator == 'or')):
            return True
        else:
            return False

    # Method to generate quadruples for factor, term, exp, sub_exp and expression
    def generateQuad(self, func, level):
        if not self.operatorStack.empty():
            if self.checkLevelToOp(level):
                rightOperand = self.operandStack.pop()
                rightType = self.typeStack.pop()
                leftOperand = self.operandStack.pop()
                leftType = self.typeStack.pop()
                operator = self.operatorStack.pop()
                #print(leftType,leftOperand,operator,rightType,rightOperand)
                if leftType == None or rightType == None:
                    resType = None
                    print("#GenerateQuadruple Error: processing variable types:",leftType,rightType)
                else:
                    resType = self.semantic.semanticCube[operator][leftType][rightType]
                if resType != 'error' and resType != None:
                    resAddr = self.getTempAddr(resType)
                    opAddr = self.semantic.operatorToKey[operator]
                    rightAddr = self.getMemAddr(rightOperand)
                    leftAddr = self.getMemAddr(leftOperand)
                    quad = Quadruple(opAddr, leftAddr,  rightAddr, resAddr)
                    self.quadList.append(quad)
                    self.quadCount += 1
                    self.operandStack.push(resAddr)
                    self.typeStack.push(resType)
                else:
                    print("#GenerateQuadruple Error:",leftType,operator,rightType,"generates",resType)
                    sys.exit()

    # Method to generate quadruples of an assignment
    def generateAssignmentQuad(self):
        if self.operatorStack.top() == '=':
            operator = self.operatorStack.pop()
            opAddr = self.semantic.operatorToKey[operator]
            val = self.operandStack.pop()
            valAddr = self.getMemAddr(val)
            res = self.operandStack.pop()
            resAddr = self.getMemAddr(res)
            self.typeStack.pop()
            quad = Quadruple(opAddr, valAddr, None, resAddr)
            self.quadList.append(quad)
            self.quadCount += 1
        else:
            print("#GenerateQuadruple Error: assignment quadruples")
            sys.exit()

    # Method to generate quadruples for print / read / return
    def generateCommonQuad(self, type):
        if self.operandStack.empty() and self.typeStack.empty():
            print("#GenerateQuadruple Error: ", type, " quadruples")
            sys.exit()
        else:
            self.typeStack.pop()
            opAddr = self.semantic.operatorToKey[type]
            res = self.operandStack.pop()
            resAddr = self.getMemAddr(res)
            #print(res, resAddr)
            quad = Quadruple(opAddr, None, None, resAddr)
            self.quadList.append(quad)
            self.quadCount += 1

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

    #
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
            print("#RemoveFalseBottom Error")
            sys.exit()

    # inserts
    def insertStackOperator(self, operator):
        self.operatorStack.push(operator)

    def insertStackOperand(self, operand):
        self.operandStack.push(operand)
        #self.operandStack.print()

    def insertStackType(self, type):
        self.typeStack.push(type)
        #self.typeStack.print()

    def insertStackJump(self, jump):
        self.jumpStack.push(jump)
        #self.jumpStack.print()

    def insertStackDim(self, dim):
        self.dimStack.push(dim)
        #self.dimStack.print()

    # tops
    def topStackOperator(self):
        return self.operatorStack.top()

    def topStackOperand(self):
        return self.operandStack.top()

    def topStackType(self):
        return self.typeStack.top()

    def topStackJump(self):
        return self.jumpStack.top()

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

    def popStackDim(self):
        self.dimStack.pop()
