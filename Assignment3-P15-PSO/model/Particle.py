import math
import random
from copy import deepcopy


class Particle:
    def __init__(self, w, p, g, l, k):
        self.weights = w
        self.prices = p
        self.limit = g
        self.min = k
        self.max = l
        self._position = [(random.randint(0, 1)) for x in range(len(w))]

        self._best_position = deepcopy(self._position)

        self._fitness = self.compute_fitness()
        self._best_fitness = deepcopy(self._fitness)
        self.compute_fitness()
        self._best_fitness = deepcopy(self._fitness)

        self._velocity = [0 for i in range(len(self._position))]

    @property
    def position(self):
        return self._position

    @staticmethod
    def create(w, p, g, l, k):
        return Particle(w, p, g, l, k)

    # @staticmethod
    # def generate(xa, xb, ya, yb):
    #     return Particle(random.uniform(xa, xb), random.uniform(ya, yb))

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, other):
        self._fitness = other
        if self._best_fitness < self._fitness:
            self._best_fitness = deepcopy(self._fitness)
            self._best_position = deepcopy(self._position)

    def compute_fitness(self):
        pric = 0
        for i in range(0, len(self._position)):
            pric += self._position[i] * self.prices[i]
        number = 0
        greut = 0

        for i in range(0, len(self._position)):
            greut += self.weights[i] * self._position[i]
            number += self._position[i]

        penalization = 0
        if number > self.max:
            penalization = (number - self.max) * 500
        if number < self.min:
            penalization = (self.min - number) * 500
        return pric - (self.limit * abs(greut - self.limit)) - penalization

    def compute_velocity(self, best_global_particle, w, c1, c2):
        newVelocity = []
        for j in range(len(self._velocity)):
            velocity_component = w * self._velocity[j] + \
                                 c1 * random.random() * (best_global_particle._position[j] - self._position[j]) + \
                                 c2 * random.random() * (self._best_position[j] - self._position[j])
            newVelocity.append(velocity_component)
        self._velocity = deepcopy(newVelocity)
        for i in range(len(self._velocity)):
            x = self.sigmoid(self._velocity[i])
            if x <= 0.5:
                self._position[i] = 0
            else:
                self._position[i] = 1

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def __str__(self):
        s = ""
        s += "Current position: " + str(self._position) + "\n with a fitness of " + str(self._fitness) + "vel" + str(self._velocity) + '\n'
        s += "Best position: " + str(self._best_position) + "\n with a fitness of " + str(self._best_fitness)
        return s
