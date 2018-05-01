from src.Main.Individual import Individual


class Population:

    def __init__(self, size, values, vertices):
        self.size = size
        self.edges = values
        self.vertices = vertices
        self.values = self.create()

    def create(self):
        val = []
        for x in range(self.size):
            edge = self.edges[:]
            ver = self.vertices[:]
            ind = Individual(edge, ver)
            val.append(ind)
        return val
