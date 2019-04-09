from operator import attrgetter
from statistics import mean


class Population:
    def __init__(self, size):
        self.popSize = size
        self.population = []

    def getPopulation(self):
        return self.population

    def setPopulation(self, pList):
        self.population = pList

    def addIndivid(self, individ):
        self.population.append(individ)

    def getMin(self):
        return min(self.population, key = attrgetter("fit"))

    def getAverageFitness(self):
        l=[]
        for x in self.population:
            l.append(x.getFitness())
        return mean(l)

    def __len__(self):
        return self.popSize

    def __getitem__(self, item):
        return self.population[item]

    def __setitem__(self, key, value):
        self.population[key] = value

    def evaluate(self):
        for x in self.population:
            x.fitness()
        return self.population
