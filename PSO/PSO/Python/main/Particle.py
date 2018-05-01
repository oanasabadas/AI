from random import randint

import copy


class Particle:
    def __init__(self, values, vertices):
        self.vertices = vertices
        # edges values (1 2),(4 5)....
        self.values = values
        # edges boolean 0 1
        self.edges = []
        self.velocity = [0 for i in range(len(values))]
        # # position of the particle
        self.position = []
        self.create()
        self.evaluate()
        self.bestPosition = self.position.copy()
        self.bestFitness = self.fitness

    def create(self):
        # a = []
        # b = []
        for i in range(len(self.values)):
            r = randint(0, 1)
            if r < 0.5:
                self.edges.append(0)
                # a.append(self.values[i])
            else:
                self.edges.append(1)
                # b.append(self.values[i])

        # self.position.append(a)
        # self.position.append(b)
        self.position = copy.deepcopy(self.edges)

    def out_bound(self, ed):
        out = {}
        for i in range(len(self.vertices)):
            out[self.vertices[i]] = []
        for i in range(len(ed)):
            out[ed[i][0]].append(ed[i][1])
            out[ed[i][1]].append(ed[i][0])
        return out

    def evaluate(self):
        self.fitness = self.fit(self.position)

    def fit(self, position):
        set1 = []
        set2 = []
        for i in range(len(self.values)):
            if self.edges[i] == 0:
                set1.append(self.values[i])
            else:
                set2.append(self.values[i])

        #
        # ok1 = self.has_triangle(self.out_bound(position[0]))
        # ok2 = self.has_triangle(self.out_bound(position[1]))
        ok1 = self.has_triangle(self.out_bound(set1))
        ok2 = self.has_triangle(self.out_bound(set2))
        if ok1 and ok2:
            return 0
        else:
            if ok1 or ok2:
                return 1
            else:
                return 2

    def has_triangle(self, out):

        visited = []
        stack = []
        stack.append("1")
        last = None
        while len(stack) > 0:
            current = stack[-1]
            stack = stack[:-1]
            if current not in visited:
                visited.append(current)
            if last != None:
                y = out[last]

            for x in out[current]:
                if x not in visited:
                    visited.append(x)
                    stack.append(x)
                else:
                    if last != None:
                        if x in y:
                            return False
            last = current
        return True

    def __str__(self):
        return str(self.position[1]) + \
               "\nedges 0 1:" + str(self.edges) + "\nvelocity: " + str(self.velocity) + \
               "\nfitness: " + str(self.fitness) + "\nbestfitness: " + str(self.bestFitness) + "\nbestPozition: " + \
               str(self.bestPosition)

    def __lt__(self, other):
        return True
