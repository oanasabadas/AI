from math import exp
from random import random


class Controller:
    def __init__(self, population, c1, c2, w):
        self.population = population
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def iteration(self):
        # pass
        neighbors = self.population.getBestParticles()
        bestNeighbors = self.population.getBestNeighbourParticle()

        # update velocity based on best neighbor and best position
        """
        vezi ca aici aio litsa de velocitati.... daca nu e bine incearca cu una singura
        """
        for i in range(self.population.size):
            for j in range(len(self.population.values[0].velocity)):
                # newVelocity = self.w * self.population.values[i].velocity[j]
                # newVelocity = newVelocity * self.c1.fitness * random() * self.population.getBestNeighbourParticle()[i].fitness
                newVelocity = self.w * self.population.values[i].velocity[j]
                # newVelocity = newVelocity + self.c1 * random() * (
                #         self.population.values[bestNeighbors[i].position[j]] - self.population.values[i].position[
                #     j])
                # newVelocity = newVelocity * self.c1 * random() * (self.population.getBestNeighbourParticle()[
                #     i].position[j]-self.population.values[i].position[j])
                newVelocity = newVelocity + self.c1 * random() * (
                        self.population.values[i].bestPosition[j] - self.population.values[i].position[j])
                newVelocity = newVelocity + self.c2 * random() * (
                        self.population.values[i].bestPosition[j] - self.population.values[i].position[j])
                # pop[i].velocity[j] = newVelocity
                if random() < 1 / (1 + exp(-newVelocity)):
                    self.population.values[i].velocity[j] = 1
                else:
                    self.population.values[i].velocity[j] = 0

        for i in range(self.population.size):
            newPosition = []
            for j in range(len(self.population.values[0].velocity)):
                newPosition.append((self.population.values[i].position[j] + self.population.values[i].velocity[j]) % 2)

            self.population.values[i].position = newPosition
        return self.population

    def __str__(self):
        return str(self.population)
