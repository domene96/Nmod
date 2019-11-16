#!/usr/bin/env python

# LIFO Stack implementantion
# Used for: OPERANDS, OPERATORS, TYPES, and JUMPS
class Stack:
    # Initialize stack
    def __init__(self):
        self.stack = []

    # Insert value into stack
    def push(self, value):
        self.stack.append(value)

    # Remove from stack, return removed item
    def pop(self):
        if self.stack:
            top = self.top()
            self.stack.pop()
            return top
        else:
            print("Nothing in stack")

    # Return first item in stack
    def top(self):
        if self.stack:
            return self.stack[-1]

    # Check if stack is empty
    def empty(self):
        return not self.stack

    # Print stack as string
    def print(self):
        return print(self.stack)

    # Clean the stack
    def clean(self):
        while not self.empty():
            self.pop()

    # Destroy stack
    def destroy(self):
        del self

# FIFO Queue implementantion
# Used for: STORING temporary and polish vector values
class Queue:
    # Initialize queue
    def __init__(self):
        self.queue = []

    # Insert value into queue
    def push(self, value):
        self.queue.append(value)

    # Remove from stack, return removed item
    def pop(self):
        if self.queue:
            top = self.top()
            self.queue.pop(0)
            return top
        else:
            print("Nothing in queue")

    # Return first item in queue
    def top(self):
        if self.queue:
            return self.queue[0]

    # Check if queue is empty
    def empty(self):
        return not self.queue

    # Print queue as string
    def print(self):
        return print(self.queue)

    # Destroy queue
    def destroy(self):
        del self

# Quadruple implementation
class Quadruple:
    # Initialize quadruple
    def __init__(self, op, leftOp, rightOp, res):
        self.operator = op
        self.leftOperand = leftOp
        self.rightOperand = rightOp
        self.result = res

    # Get quad operator symbol
    def getOperator(self):
        return self.operator

    # Get quad left operand value
    def getLeftOperand(self):
        return self.leftOperand

    # Get quad right operand value
    def getRightOperand(self):
        return self.rightOperand

    # Get quad result value
    def getResult(self):
        return self.result

    # Set quad result
    def setResult(self, res):
        self.result = res

    # Print quad data
    def print(self):
        print("[ " + str(self.operator) + ", " + str(self.leftOperand) + ", " + str(self.rightOperand) + ", " + str(self.result) + " ]")

    # Destroy quadruple
    def destroy(self):
        del self

# Data Structure for dimension information
class DimensionNode:
    # Initialize node
    def __init__(self):
        self.low = None
        self.high = None
        self.k = None
        self.dimPointer = None

    # Get lower bound of dimension
    def getDimLow(self):
        return self.low

    # Set lower bound of dimension
    def setDimLow(self, val):
        self.low = val

    # Get higher bound of dimension
    def getDimHigh(self):
        return self.high

    # Set higher bound of dimension
    def setDimHigh(self, val):
        self.high = val

    # Get k constant of dimension
    def getDimK(self):
        return self.k

    # Set k constant of dimension
    def setDimK(self, val):
        self.k = val

    # Get next dimension node
    def getDimPointer(self):
        return self.dimPointer

    # Set next dimension node
    def setDimPointer(self, val):
        self.dimPointer = val

    # Check if current dimension is last dimension
    def isLast(self):
        if self.dimPointer == None:
            return True
        else:
            return False

    # Method to clean all attributes of dimension node
    def clear(self):
        self.low = None
        self.high = None
        self.k = None
        self.dimPointer = None

    # Print dimension node
    def print(self):
        if self.dimPointer != None:
            print("[ " + str(self.low) + ", " + str(self.high) + ", " + str(self.k) + ", " + str(self.dimPointer.print()) + " ]")
        else:
            print("[ " + str(self.low) + ", " + str(self.high) + ", " + str(self.k) + ", " + str(None) + " ]")

    # Method to destroy the dimension node
    def destroy(self):
        del self

# Activation Record implementation
class ActivationRecord:
    # Initialize Activation Record
    def __init__(self, funcMem):
        # Local memory for current function, type: Memory
        self.eraMem = funcMem

    # Print activation record
    def print(self):
        1

    # Destroy activation record
    def destroy(self):
        del self
