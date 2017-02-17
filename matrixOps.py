# MatrixOps Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

"""
Matrices look like:
matrixA[row (index of sublist), col (index within sublist)]
in terms of the screen: matrixA[x][y]

We are not modifying in place; we are returning a new matrix
"""

# Scalar Multiplication
def scalarMult(scalar, matrix):
   modMatrix = []
   for rowEl in matrix:
       newRow = []
       for colEl in rowEl:
           newRow.append(colEl * scalar)
        modMatrix.append(newRow)
    return modMatrix


# Matrix Multiplication
def matrixMult(matrixA, matrixB):
    if len(
