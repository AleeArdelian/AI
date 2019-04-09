import random
import matplotlib.pyplot as plt
from statistics import mean, stdev

from Population import Population
from Individ import Individ

class Algorithm:
    def __init__(self):
        self.population = None
        self.xMin = None
        self.xMax = None
        self.yMin = None
        self.yMax = None
        self.mutP = None
        self.noIter = None
        self.noIndivides = None
        self.readParams()

    def readParams(self):
        with open('data.in', 'r') as f:
            self.xMin = float(f.readline())
            self.xMax = float(f.readline())
            self.yMin = float(f.readline())
            self.yMax = float(f.readline())
        with open('params.in', 'r') as d:
            self.mutP = float(d.readline())
            self.noIter = int(d.readline())
            self.noIndivides = int(d.readline())

    def generatePop(self, size):
        pop = Population(size)
        for x in range(0, size):
            ind = Individ(self.xMin, self.xMax, self.yMin, self.yMax)
            ind.generateIndivid()
            pop.addIndivid(ind)
        pop.evaluate()
        return pop

    def iteration(self):
        first = random.randint(0, len(self.population)-1)
        second = random.randint(0, len(self.population)-1)
        if first != second:
            ind1 = self.population[first]
            ind2= self.population[second]
            child = ind1.crossover(ind2)
            child.mutate(self.mutP)
            child.fitness()
            if ind1.getFitness() > ind2.getFitness() and ind1.getFitness() > child.getFitness():
                self.population[first] = child
            if ind1.getFitness() < ind2.getFitness() and ind2.getFitness() > child.getFitness():
                self.population[second] = child

    def statistics(self):
        fit =[]
        for x in range(30):
            val = self.run(40, 0)
            fit.append(val.getFitness())
        agv = mean(fit)
        standDev = stdev(fit)
        print("The average is: " + str(agv))
        print("The standard deviation is: " + str(standDev))

    def run(self, nrGenerated, let):
        self.population = self.generatePop(nrGenerated)
        fitList=[]
        for x in range(self.noIter):
            self.iteration()
            fitList.append(self.population.getAverageFitness())
        if let == 1:
            plt.clf()
            plt.plot(fitList)
            plt.ylabel("Fitness variation")
            plt.show()
        return self.population.getMin()

    def displayRun(self):
        val = self.run(self.noIndivides, 1)
        print("The minimum of the function is:")
        print(val)
        print(val.getFitness())

