1) git clone https://github.com/domene96/Nmod.git

optional 2) java -Xmx500M -cp ./antlr-4.7-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Nmod.g4

3) Testing:
-python3 NmodRunner.py ./tests/ArithmeticAndModules.nmod
-python3 NmodRunner.py ./tests/LogicalAndConditions.nmod
-python3 NmodRunner.py ./tests/DimensionedVariablesAndCicles.nmod
-python3 NmodRunner.py ./tests/FibonacciAndFactorial.nmod
-python3 NmodRunner.py ./tests/Traversal.nmod
-python3 NmodRunner.py ./tests/SpecialFunctions.nmod
-python3 NmodRunner.py ./tests/MatrixMultiplication.nmod
-python3 NmodRunner.py ./tests/main.nmod
