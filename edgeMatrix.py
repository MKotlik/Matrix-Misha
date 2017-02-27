# EdgeMatrix Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)


class EdgeMatrix:
    '''Class for representing and modifying an edge matrix'''

    # Point position enums
    X, Y, Z, SCALE = 0, 1, 2, 3

    # Constructor
    def __init__(self, initMatrix=None, prevObj=None, size=0):
        if initMatrix is not None:
            if type(initMatrix) is not list:
                raise TypeError(
                    "initMatrix arg of EdgeMatrix constructor must be 2d list")
            elif len(initMatrix) > 0 and len(initMatrix)[0] != 4:
                raise ValueError(
                    "initMatrix of EdgeMatrix constructor must have 4 rows")
            else:
                matrixStore = initMatrix
        elif prevObj is not None:
            matrixStore = prevObj.getMatrix()
        elif size > 0:
            matrixStore = [None] * size
        else:
            matrixStore = []

    def getMatrix(self):
        return self.matrixStore

    def addPoint(self, point):
        if type(point) is not list:
            raise TypeError(
                "addPoint method of edgeMatrix takes a 4-element list")
        elif len(point) != 4:
            raise ValueError(
                "addPoint method of edgeMatrix takes a 4-element list")
        self.matrixStore.append(point)

    def addEdge(point1, point2):
        try:
            addPoint(point1)
            addPoint(point2)
        except TypeError:
            raise TypeError(
                "addEdge method of edgeMatrix takes two 4-element lists")
        except ValueError:
            raise ValueError(
                "addEdge method of edgeMatrix takes two 4-element lists")

    def __str__(self):
        obj_str = ""
        r0 = r1 = r2 = r3 = ""
        for point in self.matrixStore:
            # Calculate maxLen for padding
            maxLen = 0
            for coord in point:
                curLen = len(str(coord))
                if curLen > maxLen:
                    maxLen = curLen
            # Create padding formatting string
            padStr = "{:>" + maxLen + "}"
            # Add each coord to respective rowStr, w/ padding
            r0 += padStr.format(point[0]) + ""
            r1 += padStr.format(point[1]) + ""
            r2 += padStr.format(point[2]) + ""
            r3 += padStr.format(point[3]) + ""
        obj_str = r0 + "\n" + r1 + "\n" + r2 + "\n" + r3 + "\n"
        return obj_str

    # __multiply__ goes here

    # __add__ goes here
