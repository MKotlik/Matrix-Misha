# Tester for Edge Matrix updates
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

import draw
import display
from edgeMatrix import EdgeMatrix
import matrixOps

# Basic matrix math tests
print "NOTE: matrices are being printed column across, row down -> incorrectly"
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
matrixNo = [[5, 5, 5, 5]]
matrixE = matrixOps.multiply(matrixNo, matrixA)  # MatrixMult, should except

# EdgeMatrix tests
eM1 = EdgeMatrix()
print eM1
