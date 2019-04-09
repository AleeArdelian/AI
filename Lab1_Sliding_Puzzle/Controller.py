
from queue import PriorityQueue


class Controller:
    def __init__(self, problem):
        self._problem = problem

    def BFS(self):
        visited = []
        queue = [[self._problem.getInitialState()]]
        while len(queue) > 0:
            steps = queue.pop(0)
            if steps[-1] not in visited:
                visited.append(steps[-1])
            if self._problem.isSolution(steps[-1]):
                return steps
            for p in self._problem.expand(steps[-1]):
                if p not in visited:
                    steps = steps + [p]
                    if self._problem.isSolution(steps[-1]):
                        return steps
                    visited.append(steps[-1])
                    queue.append(steps)
                    steps = steps[:-1]
        return None

    def GBFS(self):
        visited = []
        queue = PriorityQueue()
        queue.put([self._problem.getInitialState()])
        while not queue.empty():
            steps = queue.get()
            if steps[-1] not in visited:
                visited.append(steps[-1])
            if self._problem.isSolution(steps[-1]):
                return steps

            for p in self._problem.expand(steps[-1]):
                if p not in visited:
                    steps.append(p)
                    visited.append(steps[-1])
                    queue.put(steps)
                    steps = steps[:-1]
        return None

