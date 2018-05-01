from random import randint

import copy

from Python.main.Particle import Particle


class Swarm:

    def __init__(self, size, edges, vertices, numberNeighbour):
        self.size = size
        self.nSize = numberNeighbour
        self.edges = edges
        self.vertices = vertices
        self.values = self.create()

    def create(self):
        val = []
        for x in range(self.size):
            edge = self.edges[:]
            ver = self.vertices[:]
            ind = Particle(edge, ver)
            val.append(ind)
        return val

    def getBestNeighbourParticle(self):
        bestNeighbor = []
        neighbors = self.getBestParticles()
        for particle in range(self.size):
            for i in range(0, len(neighbors[particle])):
                bestnow = neighbors[particle][0]
                for j in range(1, len(neighbors[particle])):
                    if neighbors[particle][i].fitness > neighbors[particle][j].fitness:
                        bestnow = neighbors[particle][j]
            bestNeighbor.append(bestnow)
        return bestNeighbor

    def getBestParticles(self):
        if self.nSize > len(self.values):
            self.nSize = len(self.values)
        neighbors = []
        for i in range(len(self.values)):
            localNeighbor = []
            for j in range(self.nSize):
                x = randint(0, len(self.values) - 1)
                while x in localNeighbor:
                    x = randint(0, len(self.values) - 1)
                localNeighbor.append(self.values[x])
            neighbors.append(copy.deepcopy(localNeighbor))
        return neighbors

    def __str__(self):
        bb=""
        bestPart=self.getBestParticles()
        for i in range(len(bestPart[0])):
            bb+=str(bestPart[0][i])+"\n-----------------------------------------------"
        s = ""
        for i in range(len(self.values)):
            s += str(self.values[i]) + "\n\n"
        best = ""
        neigh = self.getBestNeighbourParticle()
        for i in range(len(neigh)):
            best += str(neigh[i]) + "\n\n"

        return "best heighbors: " + bb + "\nbest neighbor: \n=======================================================================\n" + \
               best + "\n=======================================================================\nvalues: --------------------------------------------------\n" + s
