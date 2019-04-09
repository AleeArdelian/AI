from texttable import Texttable


class Puzzle:
    def __init__(self):
        self._board = []
        self._l = 0
        self._finalState = []
        self._emptySpaceX = 0
        self._emptySpaceY = 0
        self._heuristic =0

    def setBoard(self, board, final):
        self._board = board
        self._finalState = final
        self._l = len(self._board[0])
        self._emptySpaceX, self._emptySpaceY = self.getBlankPosition()

    def setFinalState(self, b):
        self._finalState = b

    def setLen(self, x):
        self._l = x

    def setEmptySpace(self, x, y):
        self._emptySpaceX = x
        self._emptySpaceY = y

    def getCoordinates(self, val):
        for x in range(self._l):
            for y in range(self._l):
                if self._board[x][y] == val:
                    return x, y

    def getBoard(self):
        return self._board

    def getX(self):
        return self._emptySpaceX

    def getHeuristic(self):
        return self._heuristic

    def setHeuristic(self, h):
        self._heuristic = h

    def getY(self):
        return self._emptySpaceY

    def getLen(self):
        return self._l

    def getEmpty(self):
        return self._emptySpaceX, self._emptySpaceY

    def getBlankPosition(self):
        for x in range(self._l):
            for y in range(self._l):
                if self._board[x][y] == '0':
                    return x, y

    def printTable(self):
        table = Texttable()
        for i in self._board:
            table.add_row(i)
        print(table.draw())

    def heuristics(self):  # final state
        distance = 0
        for x in range(self._l):
            for y in range(self._l):
                if self._board[x][y] != self._finalState[x][y]:
                    distance += 1
        return distance

    def __lt__(self, other):
        return self._heuristic < other.getHeuristic()

    def __eq__(self, other):
        for i in range(self._l):
            for j in range(self._l):
                if self._board[i][j] != other.getBoard()[i][j]:
                    return False
        return True
