import statistics

from model.Swarm import Swarm
from model.Particle import Particle
import matplotlib.pyplot as plt


class Algorithm:

    def __init__(self):
        with open("Dates.txt") as f:
            self._particles_number = int(f.readline())
            self._l = int(f.readline())
            self._k = int(f.readline())
            self._g = int(f.readline())
            self._w = float(f.readline())
            self._c1 = float(f.readline())
            self._c2 = float(f.readline())
            self._iterations = int(f.readline())
        self.weights = [10, 20, 30, 40, 50, 40, 50]
        self.prices = [12, 13, 10, 10, 20, 10, 10]
        self._swarm = None
        self.new_swarm(self._particles_number)
        self._DF = True

    def new_swarm(self, particles_number):
        swarm = []
        for x in range(particles_number):
            p = Particle.create(self.weights, self.prices, self._g, self._l, self._k)
            swarm.append(p)
        self._swarm = Swarm(swarm, particles_number, self._w, self._c1, self._c2)

    @property
    def swarm(self):
        return self._swarm

    def run(self, swarm=None):
        if swarm is None:
            self.new_swarm(self._particles_number)
        else:
            self.new_swarm(swarm)

        fitnesses = []
        for i in range(self._iterations):
            for particle in self._swarm.get_particles():
                particle.fitness = particle.compute_fitness()
            self._swarm.update_best()
            part = self._swarm.global_best
            if self._DF is True:
                print(str(i) + "\n" + str(part) + "\n\n")
            for particle in self._swarm.get_particles():
                particle.compute_velocity(self._swarm.global_best,self._w, self._c1, self._c2)
            fitnesses.append(self._swarm.global_best.fitness)

        best = self._swarm.global_best
        if self._DF is True:
            print("\nThe detected best particle in " + str(self._iterations) + " iterations is " + str(best.position) )

            # plt.clf()
            # plt.plot(fitnesses)
            # plt.ylabel("Fitness variation")
            # plt.show()
        return best

    def stats(self):
        bests = []
        temp_iterations = self._iterations
        self._DF = False
        self._iterations = 1000
        for i in range(30):
            particle = self.run(40)
            bests.append(particle.fitness)
        mean = statistics.mean(bests)
        stdev = statistics.stdev(bests)
        print("In 30 runs with 1000 iterations and a swarm of 40 particles: ")
        print("\t -> the average minimum point found is: " + str(mean))
        print("\t -> the standard deviation is: " + str(stdev))
        self._DF = True
        self._iterations = temp_iterations
