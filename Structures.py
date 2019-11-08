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
        return str(self.stack)

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
        return str(self.queue)

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
        print("[ " + self.operator + ", " + self.leftOperand + ", " + self.rightOperand + ", " + self.result + " ]")

# Activation Record implementation
class ActivationRecord:
    # Initialize Activation Record
    def __init__(self, funcMem):
        # Local memory for current function, type: Memory
        self.eraMem = funcMem

    # Print activation record
    def print(self):
        1
