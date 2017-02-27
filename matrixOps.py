# MatrixOps Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

from pprint import pprint

"""
Matrices look like:
matrixA[col (index of sublist), row (index within sublist)]
in terms of the edge matrix: matrixA[position][point]

We are not modifying in place; we are returning a new matrix
"""

"""
# Returns string representation of matrix
def toString(matrix):
    obj_str = ""
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return str(matrix)
    for rowN in range(len(matrix[0])):
        # Calculate maxLen for padding
        maxLen = 0
        for coord in point:
            curLen = len(str(coord))
            if curLen > maxLen:
                maxLen = curLen
        # Create padding formatting string
        padStr = "{:>" + str(maxLen) + "}"
        # Add each coord to respective rowStr, w/ padding
        r0 += padStr.format(point[0]) + ""
        r1 += padStr.format(point[1]) + ""
        r2 += padStr.format(point[2]) + ""
        r3 += padStr.format(point[3]) + ""
    obj_str = r0 + "\n" + r1 + "\n" + r2 + "\n" + r3 + "\n"
    return obj_str
"""


# Prints the matrix
def printM(matrix):
    for col in matrix:
        print str(col)


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
    for colEl in matrix:
        newCol = []
        for rowEl in colEl:
            newCol.append(rowEl * scalar)
        modMatrix.append(newCol)
    return modMatrix


# Matrix Multiplication
def matrixMult(matrixA, matrixB):
    # Check that both matrices are not empty
    if (len(matrixA) == 0 or len(matrixA[0]) == 0 or
            len(matrixB) == 0 or len(matrixB[0]) == 0):
        print "matrixOps ERROR: (matrixMult) cannot multiply an empty matrix"
        return None
    # Check that numbers of cols in A matches number of rows in B
    if (len(matrixA) != len(matrixB[0])):
        print "matrixOps ERROR: (matrixMult) num of cols in 1st matrix doesn't \
        match num of rows in 2nd matrix"
        return None
    # Create new matrix, and fill it with multiplication product
    product = []
    # Iterate over dimensions of product matrix (thru each col, thru each cell)
    # Dimensions: num cols in B * num rows in A
    for colN in range(len(matrixB)):
        col = []  # Create new column to fill
        for rowN in range(len(matrixA[0])):
            cellProd = 0
            # Iterate over els to be multiplied, equal to num cols in A
            for elNum in range(len(matrixA)):
                cellProd += matrixA[elNum][rowN] * matrixB[colN][elNum]
            col.append(cellProd)
        product.append(col)
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
    # Left identity needs to match num rows in matrix
    return createIdentity(matrix, len(matrix[0]))


# Create the right identity matrix for a given matrix
# Aka the identity matrix that would be the right operand
def getRightIdentity(matrix):
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        print "matrixOps ERROR: (identity) cannot create identity for \
        an empty matrix"
        return None
    # Right identity needs to match num cols in matrix
    return createIdentity(matrix, len(matrix))


# Creates identity matrix with given dimension
def createIdentity(matrix, numEls):
    identity = []
    for colN in range(numEls):
        col = [0] * numEls
        col[colN] = 1
        identity.append(col)
    return identity
