from copy import deepcopy
from statistics import mean


class Swarm:
    def __init__(self, particles, no_particles, w, c1, c2):
        self._particles = particles
        self._no_particles = no_particles
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self._best_global_particle = self._particles[0]

    @property
    def global_best(self):
        return self._best_global_particle

    def get_particles(self):
        return self._particles

    def update_best(self):
        for part in self._particles:
            if part.fitness < self._best_global_particle.fitness:
                self._best_global_particle = deepcopy(part)

    def average_fitness(self):
        return mean([p.fitness for p in self._particles])

    def __str__(self):
        s = ""
        for part in self._particles:
            s += str(part) + "\n\n"
        return s

