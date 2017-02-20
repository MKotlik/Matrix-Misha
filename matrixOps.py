# MatrixOps Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

from pprint import pprint

"""
Matrices look like:
matrixA[row (index of sublist), col (index within sublist)]
in terms of the screen: matrixA[x][y]

We are not modifying in place; we are returning a new matrix
"""


def printMatrix(matrix):
    pprint(matrix)


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
    # Check that both matrices are not empty
    if (len(matrixA) == 0 or len(matrixA[0]) == 0 or
            len(matrixB) == 0 or len(matrixB[0]) == 0):
        print "matrixOps ERROR: cannot multiply an empty matrix"
        return None
    # Check that numbers of cols in A matches number of rows in B
    if (len(matrixA[0]) != len(matrixB)):
        print "matrixOps ERROR: (matrixMult) num of cols in 1st matrix doesn't \
            match num of rows in 2nd matrix"
        return None
    # Create new matrix, and fill it with multiplication product
    product = []
    for rowN in range(len(matrixA)):
        row = []
        for colN in range(len(matrixB[0])):
            cellProd = 0
            for elNum in range(len(matrixB)):
                cellProd += matrixA[rowN][elNum] * matrixB[elNum][colN]
            row.append(cellProd)
        product.append(row)
    return product
