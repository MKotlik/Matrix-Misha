# EdgeMatrix Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)


class EdgeMatrix:
    '''Class for representing and modifying an edge matrix'''

    # Point position enums
    X, Y, Z, SCALE = 0, 1, 2, 3

    # Constructor
    def __init__(self, initMatrix=None, prevObj=None):
        if initMatrix is not None:
            if type(initMatrix) is not list:
                raise TypeError(
                    "initMatrix arg of EdgeMatrix constructor must be 2d list")
            elif len(initMatrix) > 0 and len(initMatrix[0]) != 4:
                raise ValueError(
                    "initMatrix of EdgeMatrix constructor must have 4 rows")
            else:
                self.matrixStore = initMatrix
        elif prevObj is not None:
            self.matrixStore = prevObj.getMatrix()
        else:
            self.matrixStore = []

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

    def addEdge(self, point1, point2):
        try:
            self.addPoint(point1)
            self.addPoint(point2)
        except TypeError:
            raise TypeError(
                "addEdge method of edgeMatrix takes two 4-element lists")
        except ValueError:
            raise ValueError(
                "addEdge method of edgeMatrix takes two 4-element lists")

    def __str__(self):
        if len(self.matrixStore) == 0:
            return "[]"
        else:
            obj_str = ""
            rowList = ["|"] * 4
            for point in self.matrixStore:
                # Calculate maxLen for padding
                maxLen = 0
                for coord in point:
                    curLen = len(str(coord))
                    if curLen > maxLen:
                        maxLen = curLen
                # Create padding formatting string
                padStr = "{:>" + str(maxLen) + "}"
                # Add each coord to respective rowStr, w/ padding
                rowList[0] += padStr.format(point[0]) + " | "
                rowList[1] += padStr.format(point[1]) + " | "
                rowList[2] += padStr.format(point[2]) + " | "
                rowList[3] += padStr.format(point[3]) + " | "
            for row in rowList:
                obj_str += row[:-1] + "\n"
            return obj_str[:-1]

    # __multiply__ goes here

    # __add__ goes here
