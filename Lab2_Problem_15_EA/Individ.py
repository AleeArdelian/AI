import random
import math


class Individ:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.x = None
        self.y = None
        self.fit = None

    def generateIndivid(self):
        x = random.uniform(self.xMin, self.xMax)
        y = random.uniform(self.yMin, self.yMax)
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getFitness(self):
        return self.fit

    def fitness(self):
        fit = math.sin(self.x + self.y) + (self.x - self.y) * (self.x - self.y) - 1.5 * self.x + 2.5 * self.y + 1
        self.fit = fit

    def crossover(self, individ):
        ind = Individ(self.xMin, self.xMax, self.yMin, self.yMax)
        x = random.uniform(self.x, self.y)
        y = random.uniform(individ.getY(), individ.getY())
        ind.setX(x)
        ind.setY(y)
        return ind

    def mutate(self, probability):
        if probability > random.random():
            gene = random.randint(1, 2)
            if gene == 1:
                x = random.uniform(self.xMin, self.xMax)
                self.x = x
            elif gene == 2:
                y = random.uniform(self.yMin, self.yMax)
                self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)
