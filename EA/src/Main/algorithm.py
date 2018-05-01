from random import randint

import copy

from src.Main.Individual import Individual
from src.Main.Population import Population


class Algorithm:

    def __init__(self, graph, probability, nr):
        self.graph = graph
        self.probability = probability
        self.population = Population(nr, graph.edges, graph.vertices)

    def crossover(self, ind1, ind2):
        r = randint(0, ind1.length - 1)
        off = []
        for i in range(ind1.length):
            if i < r:
                off.append(ind1.edges[i])
            else:
                off.append(ind2.edges[i])
        new = Individual(self.graph.edges, ind1.vertices)
        new.edges=off
        return new

    def iteration(self):
        i1 = randint(0, self.population.size - 1)
        i2 = randint(0, self.population.size - 1)
        val = self.population.values
        if i1 != i2:
            c = self.crossover(val[i1], val[i2])
            c.mutate(self.probability)
            f1 = val[i1].fitness()
            f2 = val[i2].fitness()
            fc = c.fitness()
            cc = copy.deepcopy(c)
            if (f1 <= f2) and (f1 < fc):
                val[i1] = cc
            if (f2 <= f1) and (f2 < fc):
                val[i2] = cc
