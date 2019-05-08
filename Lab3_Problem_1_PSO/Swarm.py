import copy
from random import randint
from statistics import mean

from Particle import Particle


class Swarm:
    def __init__(self, l, k, g, grams, prices, count):
        self.l = l
        self.k = k
        self.g = g
        self.grams = grams
        self.prices = prices
        self.count = count
        self.population = [Particle(l, k, g, grams, prices) for x in range(count)]
        self._globalBest = self.population[0]

    def getPopulation(self):
        return self.population

    @property
    def globalBest(self):
        return self._globalBest

    def updateBest(self):
        for part in self.population:
            if part.fitness < self._globalBest.fitness:
                self._globalBest = copy.deepcopy(part)

    def averageFitness(self):
        return mean([p.fitness for p in self.population])

    def selectNeighbors(self, nsize):
        if nsize > len(self.population):
            nsize = len(self.population)
        neighbors = []
        for i in range(len(self.population)):
            localNeighbor = []
            for j in range(nsize):
                x = randint(0, len(self.population) - 1)
                while x in localNeighbor:
                    x = randint(0, len(self.population) - 1)
                localNeighbor.append(x)
            neighbors.append(copy.deepcopy(localNeighbor))
        return neighbors

    def newPopulation(self):
        self.population = [Particle(self.l, self.k, self.g, self.grams, self.prices) for x in range(self.count)]

    @globalBest.setter
    def globalBest(self, value):
        self._globalBest = value
