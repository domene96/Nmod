#!/usr/bin/env python

# Semantic implementation
class Semantic:
    # Semantic Types
    semanticCube = {
        '+':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'float',
            },
            'float':{
                'int': 'float',
                'char': 'error',
                'float': 'float',
            },
            'char':{
                'int': 'error',
                'char': 'char[]',
                'float': 'error',
            }
        },
        '-':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'float',
            },
            'float':{
                'int': 'float',
                'char': 'error',
                'float': 'float',
            },
            'char':{
                'int': 'error',
                'char': 'error',
                'float': 'error',
            }
        },
        '*':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'float',
            },
            'float':{
                'int': 'float',
                'char': 'error',
                'float': 'float',
            },
            'char':{
                'int': 'error',
                'char': 'error',
                'float': 'error',
            }
        },
        '/':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'float',
            },
            'float':{
                'int': 'float',
                'char': 'error',
                'float': 'float',
            },
            'char':{
                'int': 'error',
                'char': 'error',
                'float': 'error',
            }
        },
        '<':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        },
        '>':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        },
        '<=':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        },
        '>=':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        },
        '==':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        },
        '=':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'float',
            },
            'float':{
                'int': 'float',
                'char': 'error',
                'float': 'float',
            },
            'char':{
                'int': 'error',
                'char': 'char',
                'float': 'error',
            }
        },
        '&&':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        },
        '||':{
            'int':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'float':{
                'int': 'int',
                'char': 'error',
                'float': 'int',
            },
            'char':{
                'int': 'error',
                'char': 'int',
                'float': 'error',
            }
        }
    }

    # Operators to number
    operatorToKey = {
        '=':5,
        '+':6,
        '-':7,
        '*':8,
        '/':9,
        '>':10,
        '<':11,
        '>=':12,
        '<=':13,
        'equal':14,
        'and':15,
        'or':16,
        'gotoF':17,
        'gotoV':18,
        'goto':19,
        'print':20,
        'read':21,
        'return':22,
        'gosub':23,
        'endproc':24
    }

    # Type to number
    typeToKey = {
        # 'error':0,
        'void':1,
        'int':2,
        'float':3,
        'char':4
    }
