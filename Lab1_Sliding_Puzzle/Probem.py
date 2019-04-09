from copy import deepcopy
from State import Puzzle


class Problem:
    def __init__(self, filename, initialState, finalState):
        self._filename = filename
        self._initialState = initialState
        self._finalState = finalState
        self._size = 0
        self.loadFromFile()

    def stateFromLine(self, line):
        state = [[] for x in range(self._size)]
        for x in range(self._size):
            for y in range(self._size):
                state[x].append(line[x * self._size + y])
        return state

    def loadFromFile(self):
        f = open(self._filename, "r")
        contents = f.read().split('\n')
        self._size = int(contents[0])
        board1 = self.stateFromLine(contents[1].split(' '))
        board2 = self.stateFromLine(contents[2].split(' '))
        self._initialState.setBoard(board1, board2)
        self._finalState.setBoard(board2, board2)
        h1 = self.heuristics(board1)
        h2 = self.heuristics(board2)
        self._initialState.setHeuristic(h1)
        self._finalState.setHeuristic(h2)

    def isSolution(self, board):
        #print(board.getBoard())
        return board.getBoard() == self._finalState.getBoard()

    def getInitialState(self):
        return self._initialState

    def getFinalState(self):
        return self._finalState

    def heuristics(self, state):  # hamming distance
        #distance = 0
        #for x in range(self._size):
         #   for y in range(self._size):
          #      if state[x][y] != self._finalState.getBoard()[x][y]:
           #         distance += 1
        #return distance

        distance = 0
        for x in range(self._size):
            for y in range(self._size):
                #xVal, yVal = state.getCoordinates(state[x][y])
                xGoal, yGoal = self._finalState.getCoordinates(state[x][y])
                distance += abs(x - xGoal) + abs(y - yGoal)
        return distance

    def expand(self, p):
        children = []
        xPoz = [-1, 0, 1, 0]
        yPoz = [0, -1, 0, 1]
        x, y = p.getEmpty()
        for k in range(4):
            if 0 <= x + xPoz[k] < p.getLen() and 0 <= y + yPoz[k] < p.getLen():
                new_state = deepcopy(p.getBoard())
                aux = new_state[x][y]
                new_state[x][y] = new_state[x + xPoz[k]][y + yPoz[k]]
                new_state[x + xPoz[k]][y + yPoz[k]] = aux

                new_x = x + xPoz[k]
                new_y = y + yPoz[k]
                puzzle = Puzzle()
                h = self.heuristics(new_state)
                puzzle.setHeuristic(h)
                puzzle.setBoard(new_state, self._finalState.getBoard())
                puzzle.setEmptySpace(new_x, new_y)
                children.append(puzzle)
        return children
