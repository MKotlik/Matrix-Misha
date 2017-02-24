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


# Prints the matrix
def printM(matrix):
    for row in matrix:
        pprint(row)


# ++++++++++++++++++++++++ #
# MULTIPLICATION FUNCTIONS #
# ++++++++++++++++++++++++ #


# General matrix multiplication (determines operands):
def multiply(operandA, matrix):
    if type(operandA) is int:
        return scalarMult(operandA, matrix)
    elif type(operandA) is float:
        return scalarMult(operandA, matrix)
    elif type(operandA) is list:
        return matrixMult(operandA, matrix)
    elif type(operandA) is long:
        return scalarMult(operandA, matrix)
    else:
        print "matrixOps ERROR: (multiply) args must be matrices \
        or numbers"
        return None


# Scalar Multiplication
def scalarMult(scalar, matrix):
    # Check that matrix isn't empty
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        print "matrixOps ERROR: (scalarMult) cannot multiply an empty matrix"
        return None
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
        print "matrixOps ERROR: (matrixMult) cannot multiply an empty matrix"
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


# ++++++++++++++++++ #
# IDENTITY FUNCTIONS #
# ++++++++++++++++++ #


# By default, gets left identity matrix
def getIdentity(matrix):
    return getLeftIdentity(matrix)


# Create the left identity matrix for a given matrix
# Aka the identity matrix that would be the left operand
def getLeftIdentity(matrix):
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        print "matrixOps ERROR: (identity) cannot create identity for \
        an empty matrix"
        return None
    return createIdentity(matrix, len(matrix))


# Create the right identity matrix for a given matrix
# Aka the identity matrix that would be the right operand
def getRightIdentity(matrix):
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        print "matrixOps ERROR: (identity) cannot create identity for \
        an empty matrix"
        return None
    return createIdentity(matrix, len(matrix[0]))


# Creates identity matrix with given dimension
def createIdentity(matrix, numEls):
    identity = []
    for rowN in range(numEls):
        row = [0] * numEls
        row[rowN] = 1
        identity.append(row)
    return identity
