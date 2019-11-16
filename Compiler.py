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
        # Dimensioned Variables
        self.totalSize = 0
        self.r = 1
        self.dim = 1
        self.sum = 0
        self.rootDimNode = DimensionNode()
        self.currentDimNode = DimensionNode()
        self.prevDimNode = DimensionNode()
        # Quadruples
        self.quadList = []
        self.quadList2 = []
        self.quadCount = 0
        self.paramCount = 0
        self.operandStack = Stack()
        self.operatorStack = Stack()
        self.typeStack = Stack()
        self.jumpStack = Stack()
        self.dimStack = Stack()

    # PROCEDURES
    # Insert function and type to function directory
    def insertFunctionDirectory(self, func, type):
        if self.localFunc == 'global':
            opAddr = self.semantic.operatorToKey['goto']
            quad = Quadruple(opAddr, None, None, None)
            self.quadList.append(quad)
            quad = Quadruple('goto', None, None, None)
            self.quadList2.append(quad)
            self.quadCount += 1
        self.jumpStack.push(self.quadCount-1)
        if self.functionDirectory.addFunction(func, type, VariableTable(), [], None, None, None):
            return True
        else:
            print("#FunctionDeclaration Error: The function ", func, " was not declared properly")
            return False

    # CONSTANTS
    # Insert constant variable to constant memory
    def insertConstant(self, type, val):
        if val not in self.constants:
            self.constants[val] = [self.constMem.nextMemoryDirection(type), val]
            return self.constants[val][0]
        #else:
            #print("#ConstantDeclaration Info: The constant ",val," exists")

    # VARIABLES
    # Insert variable and type to variable table
    def insertVarTable(self, func, id, type):
        #print(func, id, type)
        size = self.totalSize
        self.totalSize = 0
        if size == 0:
            size = 1
        if self.functionDirectory.functionExists(func):
            if func == 'global':
                memDir = self.globalMem.reserveMemoryAddresses(self.localType, size)
            else:
                memDir = self.localMem.reserveMemoryAddresses(self.localType, size)
            self.functionDirectory.getVarTable(func).addVariable(id, type, memDir, None, size, None)
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")
        # If dimensioned variable associate dimension pointer to variable
        if size > 1:
            self.associateBaseAddr(id)

    # Get value of variable
    def getVarVal(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getValue(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getValue(id)
            else:
                print("#VariableDeclaration Error: The variable ", id, " is not defined")
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    # Get type of variable
    def getVarType(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                self.localType = self.functionDirectory.getVarTable(func).getType(id)
                return self.localType
            elif self.functionDirectory.getVarTable('global').varExists(id):
                self.localType = self.functionDirectory.getVarTable('global').getType(id)
                return self.localType
            else:
                print("#VariableDeclaration Error: The variable ", id, " is not defined")
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    # Get memory address of variable
    def getVarAddr(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getAddress(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getAddress(id)
            else:
                print("#VariableDeclaration Error: The variable ", id, " is not defined")
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    # Get total variable size of variable
    def getVarSize(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getTotalSize(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getTotalSize(id)
            else:
                print("#VariableDeclaration Error: The variable ", id, " is not defined")
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    # Get dimension pointer of variable
    def getVarDim(self, func, id):
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getVDimPointer(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getVDimPointer(id)
            else:
                print("#VariableDeclaration Error: The variable ", id, " is not defined")
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    # DIMENSIONAL VARIABLES
    # Method to initialize dimensioned variable
    def initDimVar(self):
        self.operandStack.pop()
        type = self.localType
        dimNode = DimensionNode()
        self.rootDimNode = dimNode
        self.currentDimNode = dimNode
        self.r = 1
        self.dim = 1

    # Method to set lower bound of a dimension
    def setDimLowBound(self, val):
        self.currentDimNode.low = val

    # Method to set upper bound of a dimension
    def setDimHighBound(self, val):
        if val < self.currentDimNode.low:
            print("#VariableDeclaration Error: The upper bound ", val, " must be bigger than the lower bound ", self.currentDimNode.low)
            sys.exit()
        self.currentDimNode.high = val
        self.r = self.r * (int(self.currentDimNode.high) - int(self.currentDimNode.low) + 1)

    # Method to move to next dimension
    def addDimension(self):
        self.dim += 1
        self.prevDimNode.setDimLow(self.currentDimNode.getDimLow())
        self.prevDimNode.setDimHigh(self.currentDimNode.getDimHigh())
        self.prevDimNode.setDimK(self.currentDimNode.getDimK())
        self.currentDimNode = DimensionNode()
        self.prevDimNode.setDimPointer(self.currentDimNode) #######

    # Method to calculate k of a dimension
    def calculateK(self):
        self.totalSize = self.r
        dimCant = self.dim
        self.currentDimNode = self.rootDimNode
        self.dim = 1
        self.sum = 0
        while self.dim <= dimCant:
            low = int(self.currentDimNode.getDimLow())
            high = int(self.currentDimNode.getDimHigh())
            m = self.r / (high - low + 1)
            self.r = m
            if self.dim != dimCant:
                self.currentDimNode.setDimK(m)
            self.sum = self.sum + low * m
            self.dim += 1
            if self.currentDimNode.getDimPointer() != None:
                self.currentDimNode = self.currentDimNode.getDimPointer()
        self.k = self.sum
        self.currentDimNode.setDimK(0 - self.k)

    # Method to set the base address to the variable in var table
    def associateBaseAddr(self, id):
        self.rootDimNode.print()
        self.functionDirectory.getVarTable(self.localFunc).setDimPointer(id, self.rootDimNode)

    # Method to verify a variable is dimensioned and generate quadruples
    def verifyDimVar(id):
        1

    # Method to begin dimensioned variable access
    def dimVarBegin(self):
        1# id = self.operandStack.pop()
        # verifyDimVar(id)
        # self.dim = 1
        # self.dimStack.push({id, self.dim})
        # dimNode = self.FunctionDirectory.getVarTable(self.localFunc).getDimPointer(id)
        # dimNode.print()
        # self.insertFalseBottom()

    # Method to continue dimensioned variable access, generate quadruples
    def nextDimension(self):
        1

    # Method to end dimensioned variable access
    def dimVarEnd(self):
        1

    # MAIN
    # Beginning of main
    def mainBegin(self):
        self.moduleBegin()
        self.fillGoto(0)

    # Debugging prints
    def mainEnd(self):
        self.functionDirectory.print()
        #self.printQuadruples();
        self.printQuadruples2();

    # MODULES
    # Beginning of module, clear local memory
    def moduleBegin(self):
        self.localMem.clearMemory()

    # End of module, generate endproc
    def moduleEnd(self):
        opAddr = self.semantic.operatorToKey['endproc']
        quad = Quadruple(opAddr, None, None, None)
        self.quadList.append(quad)
        quad = Quadruple('endproc', None, None, None)
        self.quadList2.append(quad)
        self.quadCount += 1

    # Method to get the memory address of the expected return in a given function
    def getModuleReturnAddr(self, func):
        if self.functionDirectory.functionExists(func):
            return self.functionDirectory.getAddress(func)
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")
            sys.exit()

    # Method to get the type of the expected return in a given function
    def getModuleReturnType(self, func):
        if self.functionDirectory.functionExists(func):
            return self.functionDirectory.getType(func)
        else:
            print("#FunctionDeclaration Error: The function ",func," is not defined")
            sys.exit()

    # PARAMETERS
    # Insert parameter type to expected params
    def insertParam(self, func, id, type):
        if self.functionDirectory.functionExists(func):
            if id not in self.functionDirectory.getParams(func):
                self.functionDirectory.getParams(func).append(type)
            else:
                print("#ParameterDeclaration Error: The parameter ", id, " exists")
        else:
            print("#FunctionDeclaration Error: The function ", func, " is not defined")

    # Incremente parameter count
    def moveParameterPointer(self):
        self.paramCount += 1

    # Validate parameter count and reset count to zero
    def resetParameterPointer(self):
        if self.paramCount == len(self.functionDirectory.getParams(self.localFunc)) - 1:
            self.paramCount = 0
            self.generateGoSub()
        else:
            print("#Parameter Error: missing parameters in function call ", self.localFunc)
            sys.exit()

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
            print("#MemoryManagement Error: Attempting to find ", id, " was not found")
            return id

    # Temporal address to store quad result
    def getTempAddr(self, type):
        return self.localMem.nextMemoryDirection(type)

    # QUADRUPLES
    # Print quadList
    def printQuadruples(self):
        i = 0
        for quad in self.quadList:
            print(i)
            quad.print()
            i += 1

    def printQuadruples2(self):
        i = 0
        for quad in self.quadList2:
            print(i)
            quad.print()
            i += 1

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
                    print("#GenerateQuadruple Error: processing variable types: ", leftType, rightType)
                else:
                    resType = self.semantic.semanticCube[operator][leftType][rightType]
                if resType != 'error' and resType != None:
                    resAddr = self.getTempAddr(resType)
                    opAddr = self.semantic.operatorToKey[operator]
                    rightAddr = self.getMemAddr(rightOperand)
                    leftAddr = self.getMemAddr(leftOperand)
                    quad = Quadruple(opAddr, leftAddr, rightAddr, resAddr)
                    self.quadList.append(quad)
                    quad = Quadruple(operator, leftOperand, rightOperand, resAddr)
                    self.quadList2.append(quad)
                    self.quadCount += 1
                    self.operandStack.push(resAddr)
                    self.typeStack.push(resType)
                else:
                    print("#GenerateQuadruple Error: ", leftType, operator, rightType, " generates ", resType)
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
            quad = Quadruple(operator, val, None, res)
            self.quadList2.append(quad)
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
            quad = Quadruple(type, None, None, res)
            self.quadList2.append(quad)
            self.quadCount += 1

    # Method to validate condition start quadruples, including gotoF
    def conditionStart(self, type):
        expType = self.typeStack.pop()
        if expType != 'int':
            print("#GenerateQuadruple Error: ", type, " expression quadruples")
            sys.exit()
        else:
            opAddr = self.semantic.operatorToKey['gotoF']
            condition = self.getMemAddr(self.operandStack.pop())
            res = self.operandStack.pop()
            quad = Quadruple(opAddr, condition, None, res)
            self.quadList.append(quad)
            quad = Quadruple('gotoF', condition, None, res)
            self.quadList2.append(quad)
            self.quadCount += 1

    # Method to generate condition end quadruples, including goto
    def conditionEnd(self):
        end = self.jumpStack.pop()
        self.fillGoto(end)

    # Method to generate condition else quadruples, including goto
    def conditionElse(self):
        opAddr = self.semantic.operatorToKey['goto']
        quad = Quadruple(opAddr, None, None, None)
        self.quadList.append(quad)
        quad = Quadruple('goto', None, None, None)
        self.quadList2.append(quad)
        self.quadCount += 1
        false = self.jumpStack.pop()
        self.jumpStack.push(self.quadCount - 1)
        self.fillGoto(false)

    # Method to generate cicle end quadruples, including goto
    def cicleEnd(self):
        end = self.jumpStack.pop()
        ret = self.jumpStack.pop()
        print(end,ret)
        opAddr = self.semantic.operatorToKey['goto']
        quad = Quadruple(opAddr, None, None, ret)
        self.quadList.append(quad)
        quad = Quadruple('goto', None, None, ret)
        self.quadList2.append(quad)
        self.quadCount += 1
        self.jumpStack.push(self.quadCount - 1)
        #self.fillGoto(end)

    # Method to generate era quadruple
    def generateERA(self, func):
        opAddr = self.semantic.operatorToKey['era']
        quad = Quadruple(opAddr, None, None, func)
        self.quadList.append(quad)
        quad = Quadruple('era', None, None, func)
        self.quadList2.append(quad)
        self.quadCount += 1

    # Method to generate parameter quadruples
    def generateActionParameter(self):
        self.generateQuad(self.localFunc, 'exp')
        opAddr = self.semantic.operatorToKey['param']
        resType = self.typeStack.pop()
        #print(opAddr,resType,self.paramCount,self.localFunc,len(self.functionDirectory.getParams(self.localFunc)))
        if self.paramCount >= len(self.functionDirectory.getParams(self.localFunc)):
            print("#Parameter Error: Parameter count out of bounds ", self.paramCount, " for call ", self.localFunc)
            sys.exit()
        else:
            paramType = self.functionDirectory.getParams(self.localFunc)[self.paramCount]
        if resType == paramType:
            parameter = "par" + str(self.paramCount)
            temp = self.getMemAddr(self.operandStack.pop())
            #print(parameter, temp)
            quad = Quadruple(opAddr, temp, None, parameter)
            self.quadList.append(quad)
            quad = Quadruple('param', temp, None, parameter)
            self.quadList2.append(quad)
            self.quadCount += 1
        else:
            print("#GenerateQuadruple Error: Type mismatch in action parameter quadruples, expected: ", paramType, " , received: ", resType)

    # Method to generate gosub quadruple
    def generateGoSub(self):
        resType = self.functionDirectory.getType(self.localFunc)
        resAddr = self.getTempAddr(resType)
        opAddr = self.semantic.operatorToKey['gosub']
        quad = Quadruple(opAddr, self.localFunc, None, resAddr)
        self.quadList.append(quad)
        quad = Quadruple('gosub', self.localFunc, None, resAddr)
        self.quadList2.append(quad)
        self.quadCount += 1

    # Method to fill goto position with current quadruples count
    def fillGoto(self, pos):
        print(self.quadList[pos].getOperator())
        if self.quadList[pos].getOperator() == '17' or self.quadList[pos].getOperator() == '18' or self.quadList[pos].getOperator() == '19':
            self.quadList[pos].setResult(self.quadCount)
            self.quadList2[pos].setResult(self.quadCount)
        else:
            print("#GenerateQuadruple Error: While FILL goto quadruples for pos ", pos)
            #sys.exit()

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
        self.jumpStack.print()

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
