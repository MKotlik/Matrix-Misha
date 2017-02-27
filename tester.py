# Tester for Edge Matrix updates
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

import draw
import display
import edgeMatrix
import matrixOps

# Basic matrix math tests
matrixA = [[1, 2], [4, 5], [7, 8]]
matrixOps.printM(matrixA)
print "---------------"
matrixB = [[13, 17, 23], [2, 3, 7]]
matrixOps.printM(matrixB)
print "---------------"
matrixC = matrixOps.multiply(3, matrixA)  # Scalar mult
matrixOps.printM(matrixC)
print "---------------"
matrixD = matrixOps.multiply(matrixA, matrixB)  # MatrixMult, should work
matrixOps.printM(matrixD)
print "---------------"
matrixE = matrixOps.multiply(matrixB, matrixA)  # MatrixMult, should except
