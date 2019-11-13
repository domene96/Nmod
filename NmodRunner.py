#!/usr/bin/env python

import sys
from antlr4 import *
from NmodLexer import NmodLexer
from NmodParser import NmodParser
from antlr4.error.ErrorListener import ErrorListener

class NmodErrorListener (ErrorListener):
    def __init__(self):
        super(NmodErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print('#SyntaxError -> Error: line',line,'column',column,msg)
        sys.exit()

def main(argv):
    input = FileStream(argv[1], encoding = 'utf8')
    lexer = NmodLexer(input)
    stream = CommonTokenStream(lexer)
    parser = NmodParser(stream)
    parser._listeners = [NmodErrorListener()]
    tree = parser.program()
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
