#!/usr/bin/env python

import sys
from Error import *
from Structures import *
from Semantic import *
from FunctionDirectory import *
from VirtualMachine import *

# Compiler implementation
class Compiler:
    _INT = 'int'
    _FLOAT = 'float'

    # Initialize Compiler
    def __init__(self):
        # Errors
        self.error = Error("", False, False)
        # Semantics
        self.semantic = Semantic()
        # Procedures (Functions)
        self.functionDirectory = FunctionDirectory()
        self.localMemHandler = {}
        # Variables
        self.localFunc = ''
        self.localType = ''
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
        # Debug flag
        self.debug = 2 # 0 Memory or FuncDir or Var error, 1 current issues, 2 print quads, 3 print funcDir, 4 resolved issues, 5 print memory before VM and stacks upon insertion, 6 other warnings/info

    # Methods to handle memory directions which store memory directions
    def checkVariable(self, resAddr, type):
        if str(resAddr)[0] == '¿':
            resAddr = int(resAddr[1:])
            type = 'int'
        return resAddr, type

    # MEMORY
    # Get memory address of id
    def getMemAddr(self, id):
        # Check local memory
        if self.functionDirectory.getVarTable(self.localFunc).varExists(id):
            return self.functionDirectory.getVarTable(self.localFunc).getAddress(id)
        # Check global memory
        elif self.functionDirectory.getVarTable('global').varExists(id):
            return self.functionDirectory.getVarTable('global').getAddress(id)
        # Check constant memory
        elif self.functionDirectory.constMem.findVal(id, 'int') != False:
            return self.functionDirectory.constMem.findVal(id, 'int')
        elif self.functionDirectory.constMem.findVal(id, 'float') != False:
            return self.functionDirectory.constMem.findVal(id, 'float')
        elif self.functionDirectory.constMem.findVal(id, 'char') != False:
            return self.functionDirectory.constMem.findVal(id, 'char')
        else:
            if self.debug >= 6:
                print("#COMPILATION WARNING MemoryManagement: Attempting to find " + str(id) + " was not found")
            return id

    # Temporal address to store quad result
    def getTempAddr(self, type):
        return self.functionDirectory.localMem.nextMemoryDirection(type)

    # PROCEDURES
    # Insert function and type to function directory
    def insertFunctionDirectory(self, func, type):
        if self.functionDirectory.addFunction(func, type, VariableTable(), [], None, None, None):
            return True
        else:
            msg = "#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " was not declared properly"
            self.error = Error(msg, True, True)
            self.error.revise()

    # CONSTANTS
    # Insert constant variable to constant memory
    def insertConstant(self, type, val):
        if self.debug >= 4:
            print("add ct ", type, val)
        if self.functionDirectory.constMem.findVal(val, type) == False:
            addr = self.functionDirectory.constMem.nextMemoryDirection(type)
            self.functionDirectory.constMem.setValueAtAddress(addr, val)
        else:
            msg = "#COMPILATION INFO ConstantDeclaration: The constant " + str(val) + " exist"
            self.error = Error(msg, False, False)
            self.error.revise()

    # VARIABLES
    # Method to remove brackets from id
    def cutID(self, id):
        if id.find('[') > 0:
            id = id[:id.find('[')]
        return id

    # Insert variable and type to variable table
    def insertVarTable(self, func, id, type):
        id = self.cutID(id)
        size = self.totalSize
        self.totalSize = 0
        if size == 0:
            size = 1
        if self.functionDirectory.functionExists(func):
            if self.debug >= 4:
                print("add var ", id, self.localType, size)
            if func == 'global':
                memDir = self.functionDirectory.globalMem.reserveMemoryAddresses(self.localType, size)
            else:
                memDir = self.functionDirectory.localMem.reserveMemoryAddresses(self.localType, size)
            self.functionDirectory.getVarTable(func).addVariable(id, type, memDir, None, size, None)
        else:
            msg = "#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined"
            self.error = Error(msg, True, True)
            self.error.revise()
        # If dimensioned variable associate dimension pointer to variable
        if size > 1:
            self.associateBaseAddr(id)

    # Get value of variable
    def getVarVal(self, func, id):
        id = self.cutID(id)
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getValue(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getValue(id)
            else:
                msg = "#COMPILATION ERROR VariableDeclaration: The variable " + str(id) + " is not defined"
                self.error = Error(msg, True, True)
                self.error.revise()
        else:
            msg = "#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined"
            self.error = Error(msg, True, True)
            self.error.revise()

    # Get type of variable
    def getVarType(self, func, id):
        id = self.cutID(id)
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                self.localType = self.functionDirectory.getVarTable(func).getType(id)
                return self.localType
            elif self.functionDirectory.getVarTable('global').varExists(id):
                self.localType = self.functionDirectory.getVarTable('global').getType(id)
                return self.localType
            else:
                msg = "#COMPILATION ERROR VariableDeclaration: The variable " + str(id) + " is not defined"
                self.error = Error(msg, True, True)
                self.error.revise()
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # Get memory address of variable
    def getVarAddr(self, func, id):
        id = self.cutID(id)
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getAddress(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getAddress(id)
            else:
                sys.exit("#COMPILATION ERROR VariableDeclaration: The variable " + str(id) + " is not defined")
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # Get total variable size of variable
    def getVarSize(self, func, id):
        id = self.cutID(id)
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getTotalSize(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getTotalSize(id)
            else:
                sys.exit("#COMPILATION ERROR VariableDeclaration: The variable " + str(id) + " is not defined")
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # Get dimension pointer of variable
    def getVarDim(self, func, id):
        id = self.cutID(id)
        if self.functionDirectory.functionExists(func):
            if self.functionDirectory.getVarTable(func).varExists(id):
                return self.functionDirectory.getVarTable(func).getVDimPointer(id)
            elif self.functionDirectory.getVarTable('global').varExists(id):
                return self.functionDirectory.getVarTable('global').getVDimPointer(id)
            else:
                sys.exit("#COMPILATION ERROR VariableDeclaration: The variable " + str(id) + " is not defined")
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # DECLARING DIMENSIONAL VARIABLES
    # Method to initialize dimensioned variable
    def initDimVar(self):
        self.popStackOperand()
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
            sys.exit("#COMPILATION ERROR VariableDeclaration: The upper bound " + str(val) + " must be bigger than the lower bound ", self.currentDimNode.low)
        self.currentDimNode.high = val
        self.r = self.r * (int(self.currentDimNode.high) - int(self.currentDimNode.low) + 1)

    # Method to move to next dimension
    def addDimension(self):
        self.dim += 1
        self.prevDimNode = self.currentDimNode
        self.currentDimNode = DimensionNode()
        self.prevDimNode.setDimPointer(self.currentDimNode)

    # Method to calculate k of a dimension
    def calculateK(self):
        self.totalSize = self.r
        dimCant = self.dim
        self.currentDimNode = self.rootDimNode
        self.dim = 1
        self.sum = 0
        while self.dim <= dimCant:
            if self.debug >= 4:
                print("while k ", self.dim, dimCant)
            low = int(self.currentDimNode.getDimLow())
            high = int(self.currentDimNode.getDimHigh())
            m = self.r / (high - low + 1)
            self.r = m
            if self.dim != dimCant:
                self.currentDimNode.setDimK(m)
            self.sum = self.sum + low * m
            self.dim += 1
            if self.debug >= 4:
                print("m")
                self.currentDimNode.print()
            if self.currentDimNode.getDimPointer() != None:
                self.currentDimNode = self.currentDimNode.getDimPointer()
        self.k = self.sum
        self.currentDimNode.setDimK(0 - self.k)
        if self.debug >= 4:
            print("k")
            self.currentDimNode.print()

    # Method to set the base address to the variable in var table
    def associateBaseAddr(self, id):
        self.functionDirectory.getVarTable(self.localFunc).setDimPointer(id, self.rootDimNode)
        self.dim = 1

    # ACCESS DIMENSIONED VARIABLE
    # Method to get the base address of dimensioned variable
    def getBaseAddr(self, id):
        if self.functionDirectory.getVarTable(self.localFunc).varExists(id):
            return self.functionDirectory.getVarTable(self.localFunc).getAddress(id)
        elif self.functionDirectory.getVarTable('global').varExists(id):
            return self.functionDirectory.getVarTable('global').getAddress(id)
        else:
            sys.exit("#COMPILATION ERROR VariableDeclaration: The variable " + str(id) + " is not defined")

    # Method to verify the expression is between dimension bounds and generate quadruples
    def reviseInRange(self, top):
        # Generate revise quadruple to check value between dimension bounds
        opAddr = self.semantic.operatorToKey['revise']
        low = self.currentDimNode.getDimLow()
        high = self.currentDimNode.getDimHigh()
        lowAddr = self.getMemAddr(low)
        highAddr = self.getMemAddr(high)
        topAddr = self.getMemAddr(top)
        quad = Quadruple(opAddr, lowAddr, highAddr, topAddr)
        self.quadList.append(quad)
        quad = Quadruple('revise', low, high, topAddr)
        self.quadList2.append(quad)
        self.quadCount += 1

    # Method to verify a variable is dimensioned and generate quadruples
    def verifyDimVar(self, id):
        if self.functionDirectory.getVarTable(self.localFunc).varExists(id):
            self.currentDimNode = self.functionDirectory.getVarTable(self.localFunc).getDimPointer(id)
            return True
        elif self.functionDirectory.getVarTable('global').varExists(id):
            self.currentDimNode = self.functionDirectory.getVarTable('global').getDimPointer(id)
            return True
        else:
            return False

    # Method to begin dimensioned variable access
    def dimVarBegin(self):
        id = self.popStackOperand()
        self.popStackType()
        if self.verifyDimVar(id):
            self.insertStackDim({id, self.dim})
            self.insertFalseBottom()
        else:
            sys.exit("#COMPILATION ERROR VariableAccess: The variable " + str(id) + " is not dimensioned")

    # Method to generate dimensioned variable quadruples and verify var is dimensioned variable
    def generateDimVarQuad(self, id):
        top = self.topStackOperand()
        self.reviseInRange(top)
        if self.currentDimNode.getDimPointer() != None:
            aux = self.popStackOperand()
            self.popStackType()
            # if aux == None:
            #     sys.exit("#COMPILATION ERROR VariableAccess: Missing dimensions at variable " + str(id))
            opAddr = self.semantic.operatorToKey['*']
            resAddr = self.getTempAddr(self._FLOAT)
            m = self.currentDimNode.getDimK()
            self.insertConstant(self._FLOAT, m)
            auxAddr = self.getMemAddr(aux)
            mAddr = self.getMemAddr(m)
            quad = Quadruple(opAddr, auxAddr, mAddr, resAddr)
            self.quadList.append(quad)
            quad = Quadruple('*', auxAddr, mAddr, resAddr)
            self.quadList2.append(quad)
            self.quadCount += 1
            self.insertStackOperand(resAddr)
        if self.dim > 1:
            aux2 = self.popStackOperand()
            self.popStackType()
            aux1 = self.popStackOperand()
            self.popStackType()
            # if aux1 == None or aux2 == None:
            #     sys.exit("#COMPILATION ERROR VariableAccess: Missing dimensions at variable " + str(id))
            opAddr = self.semantic.operatorToKey['+']
            aux1Addr = self.getMemAddr(aux1)
            aux2Addr = self.getMemAddr(aux2)
            resAddr = self.getTempAddr(self._FLOAT)
            quad = Quadruple(opAddr, aux1Addr, aux2Addr, resAddr)
            self.quadList.append(quad)
            quad = Quadruple('+', aux1, aux2, resAddr)
            self.quadList2.append(quad)
            self.quadCount += 1
            self.insertStackOperand(resAddr)

    # Method to continue dimensioned variable access, generate quadruples
    def nextDimension(self, id):
        self.dim += 1
        self.insertStackDim({id, self.dim})
        self.currentDimNode = self.currentDimNode.getDimPointer()

    # Method to end dimensioned variable access
    def dimVarEnd(self, id):
        aux = self.popStackOperand()
        self.popStackType()
        tempAddr = self.getTempAddr(self._FLOAT)
        resAddr = self.getTempAddr(self._FLOAT)
        # Generate quadruple to calculate memory address
        opAddr = self.semantic.operatorToKey['+']
        k = self.currentDimNode.getDimK()
        self.insertConstant(self._FLOAT, k)
        auxAddr = self.getMemAddr(aux)
        kAddr = self.getMemAddr(k)
        quad = Quadruple(opAddr, auxAddr, kAddr, tempAddr)
        self.quadList.append(quad)
        quad = Quadruple('+', auxAddr, kAddr, tempAddr)
        self.quadList2.append(quad)
        self.quadCount += 1
        # Generate quadruple with resulting memory address
        baseAddr = self.getBaseAddr(id)
        baseAddr = '(' + str(baseAddr) + ')'
        resAddr = '¿' + str(resAddr)
        quad = Quadruple(opAddr, tempAddr, baseAddr, resAddr)
        self.quadList.append(quad)
        quad = Quadruple('+', tempAddr, baseAddr, resAddr)
        self.quadList2.append(quad)
        self.quadCount += 1
        self.insertStackOperand(resAddr)
        self.popStackOperator()
        self.popStackDim()
        self.dim = 1

    # MAIN
    # Start at main
    def initialGoto(self):
        # Generate initial goto
        opAddr = self.semantic.operatorToKey['goto']
        quad = Quadruple(opAddr, None, None, None)
        self.quadList.append(quad)
        quad = Quadruple('goto', None, None, None)
        self.quadList2.append(quad)
        self.quadCount += 1
        self.insertStackJump(self.quadCount - 1)

    # Beginning of main
    def mainBegin(self):
        self.moduleBegin()
        self.fillGoto(0)

    # Debugging prints and VM instantiation
    def mainEnd(self):
        if self.debug >= 2:
            print("QUADRUPLES")
            self.printQuadruples();
            print("-------------")
            if self.debug >= 3:
                self.functionDirectory.print()
                if self.debug >= 5:
                    self.functionDirectory.globalMem.printMemory()
                    print(self.localMemHandler)
                    self.functionDirectory.constMem.printMemory()
        # Generate END quadruple
        self.generateEnd()
        # Execute virtual machine
        vm = VirtualMachine()
        # vm.debug = self.debug
        vm.functionDirectory = self.functionDirectory
        vm.localMemHandler = self.localMemHandler
        vm.run(self.quadList)

    # MODULES
    # Beginning of module, clear local memory
    def moduleBegin(self):
        if self.debug >= 4:
            print(self.localFunc)
            self.functionDirectory.localMem.printMemory()
        self.localMemHandler[self.localFunc] = self.functionDirectory.localMem
        self.functionDirectory.localMem.clearMemory()
        self.saveFunctionGoto()

    # End of module
    def moduleEnd(self):
        # Generate endproc
        opAddr = self.semantic.operatorToKey['endproc']
        quad = Quadruple(opAddr, None, None, None)
        self.quadList.append(quad)
        quad = Quadruple('endproc', None, None, None)
        self.quadList2.append(quad)
        self.quadCount += 1
        self.functionDirectory.localMem.clearMemory()

    # Method to get the memory address of the expected return in a given function
    def getModuleReturnAddr(self, func):
        if self.functionDirectory.functionExists(func):
            if self.debug >= 4:
                print(func, self.functionDirectory.getAddress(func))
            return self.functionDirectory.getAddress(func)
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # Method to get the type of the expected return in a given function
    def getModuleReturnType(self, func):
        if self.functionDirectory.functionExists(func):
            if self.debug >= 4:
                print(func, self.functionDirectory.getType(func))
            return self.functionDirectory.getType(func)
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # PARAMETERS
    # Insert parameter type to expected params
    def insertParam(self, func, id, type):
        if self.functionDirectory.functionExists(func):
            if id not in self.functionDirectory.getParams(func):
                self.functionDirectory.getParams(func).append(type)
            else:
                sys.exit("#COMPILATION ERROR ParameterDeclaration: The parameter " + str(id) + " exists")
        else:
            sys.exit("#COMPILATION ERROR FunctionDeclaration: The function " + str(func) + " is not defined")

    # Incremente parameter count
    def moveParameterPointer(self):
        self.paramCount += 1

    # Validate parameter count and reset count to zero
    def resetParameterPointer(self):
        if self.paramCount == 0:
            self.generateGoSub()
        elif self.paramCount == len(self.functionDirectory.getParams(self.localFunc)) - 1:
            self.paramCount = 0
            self.generateGoSub()
        else:
            sys.exit("#COMPILATION ERROR ParameterCount: missing parameters in function call " + self.localFunc)

    # Validate parameter count and reset count to zero
    def resetParameterPointerSpecialFunction(self, type):
        if self.paramCount == len(self.semantic.specialFunc[type][1]) - 1:
            self.paramCount = 0
            self.generateSpecialGoSub(type)
        else:
            sys.exit("#COMPILATION ERROR ParameterCount: missing parameters in special function call " + str(type))

    # QUADRUPLES
    # Print quadList
    def printQuadruples(self):
        i = 0
        for (quad, quad2) in zip(self.quadList, self.quadList2):
            print(i)
            quad.print()
            quad2.print()
            i += 1

    # General check for linear expressions (step #4 condition)
    def checkLevelToOp(self, level):
        operator = self.topStackOperator()
        if (level == 'term' and (operator == '+' or operator == '-')) or (level == 'factor' and (operator == '*' or operator == '/')) or (level == 'exp' and (operator == 'equal' or operator == '>=' or operator == '<=' or operator == '>' or operator == '<')) or (level == 'sub_exp' and (operator == 'and' or operator == 'or')):
            return True
        else:
            return False

    # Method to generate quadruples for linear expressions
    def generateQuad(self, func, level):
        if not self.operatorStack.empty():
            if self.checkLevelToOp(level):
                rightOperand = self.popStackOperand()
                rightType = self.popStackType()
                leftOperand = self.popStackOperand()
                leftType = self.popStackType()
                operator = self.popStackOperator()
                leftOperand, leftType = self.checkVariable(leftOperand, leftType)
                rightOperand, rightType = self.checkVariable(rightOperand, rightType)
                if self.debug >= 4:
                    print(operator, leftOperand, leftType, rightOperand, rightType)
                if leftType == None or rightType == None:
                    resType = None
                    sys.exit("#COMPILATION ERROR GenerateQuadruple: processing variable types: " + str(leftType) + str(rightType))
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
                    self.insertStackOperand(resAddr)
                    self.insertStackType(resType)
                else:
                    sys.exit("#COMPILATION ERROR GenerateQuadruple: " + str(leftType) + str(operator) + str(rightType) + " generates " + str(resType))

    # Method to generate quadruples of an assignment
    def generateAssignmentQuad(self):
        if self.topStackOperator() == '=':
            operator = self.popStackOperator()
            opAddr = self.semantic.operatorToKey[operator]
            val = self.popStackOperand()
            res = self.popStackOperand()
            # if self.debug >= 1:
            #     print(res, operator, val)
            valType = self.popStackType()
            resType = self.popStackType()
            if val == self.getMemAddr(val):
                val, valType = self.checkVariable(val, valType)
            if res == self.getMemAddr(res):
                res, resType = self.checkVariable(res, resType)
            valAddr = self.getMemAddr(val)
            resAddr = self.getMemAddr(res)
            if self.debug >= 4:
                print(resAddr, res, operator, valAddr, val)
            quad = Quadruple(opAddr, valAddr, None, resAddr)
            self.quadList.append(quad)
            quad = Quadruple(operator, val, None, res)
            self.quadList2.append(quad)
            self.quadCount += 1
        else:
            sys.exit("#COMPILATION ERROR GenerateQuadruple: assignment quadruples")

    # Method to generate quadruples for print / read / end
    def generateCommonQuad(self, type):
        if self.operandStack.empty() and self.typeStack.empty():
            sys.exit("#COMPILATION ERROR GenerateQuadruple: " + str(type) + " quadruples")
        else:
            self.popStackType()
            opAddr = self.semantic.operatorToKey[type]
            res = self.popStackOperand()
            resAddr = self.getMemAddr(res)
            quad = Quadruple(opAddr, None, None, resAddr)
            self.quadList.append(quad)
            quad = Quadruple(type, None, None, res)
            self.quadList2.append(quad)
            self.quadCount += 1

    # Method to validate condition start quadruples, including gotoF
    def conditionStart(self, type):
        expType = self.popStackType()
        if expType != self._INT:
            sys.exit("#COMPILATION ERROR GenerateQuadruple: " + str(type) + " expression quadruples")
        else:
            opAddr = self.semantic.operatorToKey['gotoF']
            condition = self.popStackOperand()
            conditionAddr = self.getMemAddr(condition)
            quad = Quadruple(opAddr, condition, None, None)
            self.quadList.append(quad)
            quad = Quadruple('gotoF', condition, None, None)
            self.quadList2.append(quad)
            self.quadCount += 1
            self.insertStackJump(self.quadCount - 1)

    # Method to generate condition end quadruples, including goto
    def conditionEnd(self):
        end = self.popStackJump()
        self.fillGoto(end)

    # Method to generate condition else quadruples, including goto
    def conditionElse(self):
        false = self.popStackJump()
        opAddr = self.semantic.operatorToKey['goto']
        quad = Quadruple(opAddr, None, None, None)
        self.quadList.append(quad)
        quad = Quadruple('goto', None, None, None)
        self.quadList2.append(quad)
        self.quadCount += 1
        self.insertStackJump(self.quadCount - 1)
        self.fillGoto(false)

    # Method to generate cicle end quadruples, including goto
    def cicleEnd(self):
        end = self.popStackJump()
        ret = self.popStackJump()
        opAddr = self.semantic.operatorToKey['goto']
        quad = Quadruple(opAddr, None, None, ret)
        self.quadList.append(quad)
        quad = Quadruple('goto', None, None, ret)
        self.quadList2.append(quad)
        self.quadCount += 1
        self.fillGoto(end)

    # Method to save the quadruple position of a module
    def saveFunctionGoto(self):
        self.functionDirectory.setQuadPlace(self.localFunc, self.quadCount)

    # Method to fill goto position with current quadruples count
    def fillGoto(self, pos):
        if self.debug >= 4:
            print("Fill ", pos, " quad count ", self.quadCount)
        op = str(self.quadList[pos].getOperator())
        if op == '17' or op == '18' or op == '19':
            self.quadList[pos].setResult(self.quadCount)
            self.quadList2[pos].setResult(self.quadCount)
        else:
            sys.exit("#COMPILATION ERROR GenerateQuadruple: While FILL goto quadruples for pos " + str(pos))

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
        resType = self.popStackType()
        if self.debug >= 4:
            print(opAddr,resType,self.paramCount,self.localFunc,len(self.functionDirectory.getParams(self.localFunc)))
        if self.paramCount >= len(self.functionDirectory.getParams(self.localFunc)):
            sys.exit("#COMPILATION ERROR Parameter: Parameter count out of bounds " + str(self.paramCount) + " for call " + str(self.localFunc))
        else:
            paramType = self.functionDirectory.getParams(self.localFunc)[self.paramCount]
        if resType == paramType:
            parameter = "par" + str(self.paramCount)
            temp = self.popStackOperand()
            tempAddr = self.getMemAddr(temp)
            if self.debug >= 4:
                print(parameter, tempAddr)
            quad = Quadruple(opAddr, tempAddr, None, parameter)
            self.quadList.append(quad)
            quad = Quadruple('param', temp, None, parameter)
            self.quadList2.append(quad)
            self.quadCount += 1
        else:
            sys.exit("#COMPILATION ERROR GenerateQuadruple: Type mismatch in action parameter quadruples, expected: " + str(paramType) + " , received: " + str(resType))

    # Method to generate gosub quadruple
    def generateGoSub(self):
        res = self.functionDirectory.getQuadPlace(self.localFunc)
        opAddr = self.semantic.operatorToKey['gosub']
        quad = Quadruple(opAddr, self.localFunc, None, res)
        self.quadList.append(quad)
        quad = Quadruple('gosub', self.localFunc, None, res)
        self.quadList2.append(quad)
        self.quadCount += 1

    # Method to generate return quadruple
    def generateReturn(self):
        val = self.popStackOperand()
        valAddr = self.getMemAddr(val)
        resType = self.functionDirectory.getType(self.localFunc)
        resAddr = self.getTempAddr(resType)
        opAddr = self.semantic.operatorToKey['r_return']
        quad = Quadruple(opAddr, valAddr, None, resAddr)
        self.quadList.append(quad)
        quad = Quadruple('r_return', val, None, resAddr)
        self.quadList2.append(quad)
        self.quadCount += 1

    # Method to generate era quadruple for special functions
    def generateSpecialERA(self, type):
        if type not in self.semantic.specialFunc:
            sys.exit("#COMPILATION ERROR GenerateQuadruple Error: special function " + str(type) + " quadruples")
        else:
            # Special function ERA quadruple
            opAddr = self.semantic.operatorToKey[type]
            quad = Quadruple(opAddr, None, None, None)
            self.quadList.append(quad)
            quad = Quadruple(type, None, None, None)
            self.quadList2.append(quad)
            self.quadCount += 1

    # Method to generate paramater quadruples for special functions
    def generateSpecialActionParam(self, type):
        if type not in self.semantic.specialFunc:
            sys.exit("#COMPILATION ERROR GenerateQuadruple Error: special function " + str(type) + " quadruples")
        else:
            # Special function parameter quadruples
            self.generateQuad('global', 'exp')
            opAddr = self.semantic.operatorToKey['param']
            resType = self.semantic.specialFunc[type][0]
            if self.debug >= 4:
                print(self.paramCount, len(self.semantic.specialFunc[type][1]))
            if self.paramCount >= len(self.semantic.specialFunc[type][1]):
                sys.exit("#COMPILATION ERROR ParameterDeclaration: Parameter count out of bounds " + str(self.paramCount) + " for call " + str(type))
            else:
                paramType = self.semantic.specialFunc[type][1][self.paramCount]
            if self.debug >= 4:
                print(type, self.paramCount, resType, paramType)
            if resType == paramType:
                parameter = "par" + str(self.paramCount)
                temp = self.popStackOperand()
                tempAddr = self.getMemAddr(temp)
                if self.debug >= 4:
                    print(parameter, tempAddr)
                quad = Quadruple(opAddr, tempAddr, None, parameter)
                self.quadList.append(quad)
                quad = Quadruple('param', tempAddr, None, parameter)
                self.quadList2.append(quad)
                self.quadCount += 1
            else:
                sys.exit("#COMPILATION ERROR GenerateQuadruple: Type mismatch in action parameter quadruples, expected: " + str(paramType) + " , received: " + str(resType) + " for special function " + str(type))

    # Method to generate gosub quadruple for special functions
    def generateSpecialGoSub(self, type):
        if type not in self.semantic.specialFunc:
            sys.exit("#COMPILATION ERROR GenerateQuadruple: special function " + str(type) + " quadruples")
        else:
            # Special function GOSUB quadruple
            res = self.functionDirectory.getQuadPlace(self.localFunc)
            opAddr = self.semantic.operatorToKey['gosub']
            if self.debug >= 4:
                print(opAddr, type, None, res)
            quad = Quadruple(opAddr, type, None, res)
            self.quadList.append(quad)
            quad = Quadruple('gosub', type, None, res)
            self.quadList2.append(quad)
            self.quadCount += 1

    # Method to generate end quadruple
    def generateEnd(self):
        opAddr = self.semantic.operatorToKey['end']
        quad = Quadruple(opAddr, None, None, None)
        self.quadList.append(quad)
        quad = Quadruple('end', None, None, None)
        self.quadList2.append(quad)
        self.quadCount += 1

    # STACKS
    # false bottom
    def insertFalseBottom(self):
        self.insertStackOperator('(')

    def removeFalseBottom(self):
        if self.topStackOperator() == '(':
            self.popStackOperator()
        else:
            sys.exit("#COMPILATION ERROR RemoveFalseBottom: no false bottom to remove")

    # inserts
    def insertStackOperator(self, operator):
        self.operatorStack.push(operator)
        if self.debug >= 5:
            self.operatorStack.print()

    def insertStackOperand(self, operand):
        if isinstance(operand, str):
            operand = self.cutID(operand)
        self.operandStack.push(operand)
        if self.debug >= 5:
            self.operandStack.print()

    def insertStackType(self, type):
        self.typeStack.push(type)
        if self.debug >= 5:
            print(self.quadCount)
            self.typeStack.print()

    def insertStackJump(self, jump):
        self.jumpStack.push(jump)
        if self.debug >= 5:
            self.jumpStack.print()

    def insertStackDim(self, dim):
        self.dimStack.push(dim)
        if self.debug >= 5:
            self.dimStack.print()

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
        top = self.topStackOperator()
        if top == 'and' or top == 'or':
            return True
        return False

    def topStackOperatorComparative(self):
        top = self.topStackOperator()
        if top == '<=' or top == '>=' or top == 'equal' or top == '<' or top == '>':
            return True
        return False

    def topStackOperatorTerms(self):
        top = self.topStackOperator()
        if top == '+' or top == '-':
            return True
        return False

    def topStackOperatorFactors(self):
        top = self.topStackOperator()
        if top == '*' or top == '/':
            return True
        return False

    # pops
    def popStackOperator(self):
        return self.operatorStack.pop()

    def popStackOperand(self):
        return self.operandStack.pop()

    def popStackType(self):
        return self.typeStack.pop()

    def popStackJump(self):
        return self.jumpStack.pop()

    def popStackDim(self):
        return self.dimStack.pop()
