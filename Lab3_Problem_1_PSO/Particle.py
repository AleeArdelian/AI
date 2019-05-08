""" The class that implements a particle """
import copy
from random import randint


class Particle:
    def __init__(self, l, k, g, grams, prices):
        self.grams = grams
        self.prices = prices
        self.limit = g
        self.min = l
        self.max = k
        self._pozition = [(randint(0, 1)) for x in range(len(grams))]
        self.evaluate()
        self.velocity = [0 for i in range(len(self._pozition))]

        self._bestPozition = copy.deepcopy(self._pozition)
        self._bestFitness = self._fitness

    def fit(self, pozition, price, grams, g, max, min):
        prices = 0
        number = 0
        greut = 0
        for i in range(0, len(pozition)):
            prices += pozition[i] * price[i]
            number += pozition[i]
        for i in range(0, len(pozition)):
            greut += grams[i] * pozition[i]
        if number > max:
            return -5000
        if number < min:
            return -5000
        return prices/greut

    def evaluate(self):
        self._fitness = self.fit(self._pozition, self.prices, self.grams, self.limit, self.max, self.min)

    def evaluation(self):
        self._pozition = self.evaluate()

    @property
    def pozition(self):
        return self._pozition

    @property
    def fitness(self):
        return self._fitness

    @property
    def bestPozition(self):
        return self._bestPozition

    @property
    def bestFitness(self):
        return self._bestFitness

    @pozition.setter
    def pozition(self, newPozition):
        self._pozition = newPozition.copy()
        self.evaluate()
        if self._fitness > self._bestFitness:
            self._bestPozition = self._pozition
            self._bestFitness = self._fitness

    def update(self):
        if self._fitness > self._bestFitness:
            self._bestPozition = self._pozition
            self._bestFitness = self._fitness

    def __str__(self):
        stri = ""
        for i in self._pozition:
            stri += str(i)
        return stri
