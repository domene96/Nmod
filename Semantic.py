#!/usr/bin/env python

# Semantic implementation
class Semantic:
    _ERROR = 'error'
    _VOID = 'void'
    _INT = 'int'
    _FLOAT = 'float'
    _CHAR = 'char'
    _VISUAL = 'void' # graphics
    _STRING = 'void' # 'char[]'

    # Semantic Types
    semanticCube = {
        '+':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _FLOAT:{
                _INT: _FLOAT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _ERROR,
                _FLOAT: _ERROR,
            }
        },
        '-':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _FLOAT:{
                _INT: _FLOAT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _ERROR,
                _FLOAT: _ERROR,
            }
        },
        '*':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _FLOAT:{
                _INT: _FLOAT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _ERROR,
                _FLOAT: _ERROR,
            }
        },
        '/':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _FLOAT:{
                _INT: _FLOAT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _ERROR,
                _FLOAT: _ERROR,
            }
        },
        '<=':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
            }
        },
        '>=':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
            }
        },
        '<':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
            }
        },
        '>':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
            }
        },
        'equal':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
            }
        },
        '=':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _FLOAT:{
                _INT: _FLOAT,
                _CHAR: _ERROR,
                _FLOAT: _FLOAT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _CHAR,
                _FLOAT: _ERROR,
            }
        },
        'and':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
            }
        },
        'or':{
            _INT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _FLOAT:{
                _INT: _INT,
                _CHAR: _ERROR,
                _FLOAT: _INT,
            },
            _CHAR:{
                _INT: _ERROR,
                _CHAR: _INT,
                _FLOAT: _ERROR,
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
        'revise':23,
        'era':24,
        'param':25,
        'gosub':26,
        'endproc':27,
        'r_return':28,
        'rnom':29,
        'rexp':30,
        'rgamma':31,
        'points':32,
        'lines':33,
        'text':34,
        'barplot':35,
        'piechart':36,
        'xyplot':37,
        'densityplot':38,
        'histogram':39,
        'sin':40,
        'cos':41,
        'tan':42,
        'asin':43,
        'acos':44,
        'atan':45,
        'atan2':46,
        'log':47,
        'log10':48,
        'exponent':49,
        'f_max':50,
        'f_min':51,
        'f_range':52,
        'f_sum':53,
        'diff':54,
        'prod':55,
        'mean':56,
        'median':57,
        'quantile':58,
        'weighedmean':59,
        'rank':60,
        'var':61,
        'sd':62,
        'cor':63,
        'cov':64,
        'f_round':65,
        'transpose':66,
        'diagonal':67,
        'ginv':68,
        'rowsum':69,
        'colsum':70,
        'load':71,
        'data':72,
        'library':73,
        'rpois':74,
        'rweibull':75,
        'rbinom':76,
        'rgeom':77,
        'runif':78
    }

    # Type to number
    typeToKey = {
        _ERROR:0,
        _VOID:1,
        _INT:2,
        _FLOAT:3,
        _CHAR:4
    }

    # Special Functions
    specialFunc = {
        'rnom': [_FLOAT, [_FLOAT, _FLOAT, _FLOAT]], # n, mean, var
        'rexp': [_FLOAT, [_FLOAT, _FLOAT]], # n, rate = 1
        'rgamma': [_FLOAT, [_FLOAT, _FLOAT, _FLOAT, _FLOAT, _FLOAT, _FLOAT]], # n, shape, rate = 1, scale = 1/rate, alpha = shape, beta = scale
        'points': [_VISUAL, [_FLOAT, _FLOAT]], # x, y
        'lines': [_VISUAL, [_FLOAT, _FLOAT]], # x, y
        'text': [_VISUAL, [_FLOAT, _FLOAT, _STRING]], # x, y, label
        'barplot': [_VISUAL, [_STRING, _FLOAT, _FLOAT, _FLOAT]], # name, height, width, space
        'piechart': [_VISUAL, [_STRING, _FLOAT, _FLOAT, _FLOAT]], # name, x, y, data
        'xyplot': [_VISUAL, [_STRING, _FLOAT, _FLOAT]], # name, x, y
        'densityplot': [_VISUAL, [_STRING, _FLOAT, _FLOAT]], # name, x, y
        'histogram': [_VISUAL, [_STRING, _FLOAT, _FLOAT, _FLOAT]], # name, x, breaks, frequency
        'sin': [_FLOAT, [_FLOAT]], # atomic variables
        'cos': [_FLOAT, [_FLOAT]], # atomic variables
        'tan': [_FLOAT, [_FLOAT]], # atomic variables
        'asin': [_FLOAT, [_FLOAT]], # atomic variables
        'acos': [_FLOAT, [_FLOAT]], # atomic variables
        'atan': [_FLOAT, [_FLOAT]], # atomic variables
        'atan2': [_FLOAT, [_FLOAT]], # atomic variables
        'log': [_FLOAT, [_FLOAT]], # atomic variables
        'log10': [_FLOAT, [_FLOAT]], # atomic variables
        'exponent': [_FLOAT, [_FLOAT]], # atomic variables
        'f_max': [_FLOAT, [_FLOAT]], # dimensioned variables
        'f_min': [_FLOAT, [_FLOAT]], # dimensioned variables
        'f_range': [_FLOAT, [_FLOAT]], # dimensioned variables
        'f_sum': [_FLOAT, [_FLOAT, _FLOAT]], # sum two variables
        'diff': [_FLOAT, [_FLOAT, _FLOAT]], # rest two variables
        'prod': [_FLOAT, [_FLOAT, _FLOAT]], # factor two variables
        'mean': [_FLOAT, [_FLOAT]], # dimensioned variables
        'median': [_FLOAT, [_FLOAT]], # dimensioned variables
        'quantile': [_FLOAT, [_FLOAT]], # dimensioned variables
        'rank': [_FLOAT, [_FLOAT, _INT, _STRING]], # dimensioned variable, bool, method to tie
        'var': [_FLOAT, [_FLOAT, _FLOAT]], # dimensioned variables
        'sd': [_FLOAT, [_FLOAT]], # dimensioned variables
        'cor': [_FLOAT, [_FLOAT]], # dimensioned variables
        'cov': [_FLOAT, [_FLOAT]], # dimensioned variables
        'f_round': [_FLOAT, [_FLOAT]], # dimensioned variables
        'transpose': [_FLOAT, [_FLOAT]], # dimensioned variables
        'diagonal': [_FLOAT, [_FLOAT]], # dimensioned variables
        'rowsum': [_FLOAT, [_FLOAT]], # dimensioned variables
        'colsum': [_FLOAT, [_FLOAT]], # dimensioned variables
        'load': [_STRING, [_STRING]], # file
        'data': [_STRING, [_STRING]], #
        'library': [_STRING, [_STRING]], #
        'rpois': [_FLOAT, [_FLOAT, _FLOAT, _FLOAT]], # n, p, lambda
        'rweibull': [_FLOAT, [_FLOAT, _FLOAT, _INT]], # quantiles, probabilites, n
        'rbinom': [_FLOAT, [_FLOAT, _FLOAT, _FLOAT]], # n, trials per n, probability of success per trial
        'rgeom': [_FLOAT, [_FLOAT, _FLOAT]],
        'rbinom': [_FLOAT, [_FLOAT, _FLOAT, _FLOAT]], # n, probability of success
        'runif': [_FLOAT, [_FLOAT, _FLOAT]] # n, tests per dataset
    }
