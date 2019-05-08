import math
import statistics
from random import random
from matplotlib import pyplot as plt

class Controller:
    def __init__(self, pop, c1, c2, w):
        self._population = pop
        self.c1 = c1
        self.c2 = c2
        self.w = w

    def iteration(self, pop, neighbors, c1, c2, w):
        bestNeighbors = []
        for i in range(len(pop)):
            bestNeighbors.append(neighbors[i][0])
            for j in range(1, len(neighbors[i])):
                if (pop[bestNeighbors[i]]._fitness < pop[neighbors[i][j]]._fitness):
                    bestNeighbors[i] = neighbors[i][j]
        for i in range(len(pop)):
            for j in range(len(pop[0].velocity)):
                newVelocity = w * pop[i].velocity[j] + c1 * random() * (pop[bestNeighbors[i]].pozition[j] - pop[i].pozition[j]) + c2 * random() * (pop[i].bestPozition[j] - pop[i].pozition[j])
                pop[i].velocity[j] = newVelocity
        for i in range(len(pop)):
            newPozition = []
            for j in range(len(pop[0].velocity)):
                x = self.sigmoid(pop[i].velocity[j])
                if x <= 0.5:
                    newPozition.append(0)
                else:
                    newPozition.append(1)
            pop[i]._pozition = newPozition
            pop[i].evaluate()
            pop[i].update()
        return pop

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def run(self, noIterations):
        P = self._population.getPopulation()
        neighborhoods = self._population.selectNeighbors(10)
        for i in range(noIterations):
            P = self.iteration(P, neighborhoods, self.c1, self.c2, self.w)
        best = 0
        for i in range(1, len(P)):
            if P[i]._fitness > P[best]._fitness:
                best = i
        a = P[best]._pozition
        self._population.newPopulation()
        return a

    def runForPlot(self, noIterations):
        P = self._population.getPopulation()
        neighborhoods = self._population.selectNeighbors(5)
        for i in range(noIterations):
            P = self.iteration(P, neighborhoods, self.c1, self.c2, self.w)

        Finesses = []
        for i in range(1, len(P)):
            Finesses.append(P[i]._fitness)
        return Finesses

    def stat(self, noIterations):
        minValues = [self.run(noIterations)[1] for x in range(30)]
        return statistics.mean(minValues), statistics.stdev(minValues)

    def ploting(self, noIterations):
        values = self.runForPlot(noIterations)
        plt.plot(values)
        plt.show()
