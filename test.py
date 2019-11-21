#!/usr/bin/env python

import sys
from Structures import *

def testDimPointer():
    first = DimensionNode()
    prev = first

    prev.setDimLow(3)
    prev.setDimHigh(7)
    second = DimensionNode()
    prev.setDimPointer(second)

    second.setDimLow(-5)
    second.setDimHigh(8)
    third = DimensionNode()
    second.setDimPointer(third)

    third.setDimLow(7)
    third.setDimHigh(9)
    fourth = DimensionNode()
    third.setDimPointer(fourth)

    fourth.setDimLow(-3)
    fourth.setDimHigh(6)
    fourth.setDimPointer(None)

    first.print()

testDimPointer()
