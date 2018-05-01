from random import random, randint


class Individual:

    def __init__(self, values, vertices):
        self.vertices = vertices
        self.values = values
        self.length = len(values)
        self.edges = []
        self.set1 = []
        self.set2 = []
        self.create()
        self.out1 = self.out_bound(self.set1)
        self.out2 = self.out_bound(self.set2)

    def out_bound(self, ed):
        out = {}
        for i in range(len(self.vertices)):
            out[self.vertices[i]] = []
        for i in range(len(ed)):
            out[ed[i][0]].append(ed[i][1])
            out[ed[i][1]].append(ed[i][0])
        return out

    def create(self):

        for i in range(self.length):
            r = randint(0, 1)
            if (r < 0.5):
                self.edges.append(0)
                self.set1.append(self.values[i])
            else:
                self.edges.append(1)
                self.set2.append(self.values[i])

    def mutate(self, probMutation):
        if probMutation > random():
            k = randint(0, len(self.edges) - 1)
            self.edges[k] = 1 - self.edges[k]

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

    def fitness(self):
        ok1 = self.has_triangle(self.out1)
        ok2 = self.has_triangle(self.out2)
        if ok1 and ok2:
            return 20+(len(self.edges))/2-len(self.set1)
        else:
            if ok1 or ok2:
                return 10+(len(self.edges))/2-len(self.set1)
            else:
                return 0+(len(self.edges))/2-len(self.set1)

    def __str__(self):
        return str(self.set1) + "   set2:     " + str(self.set2) + "  edges 0 1: " + str(self.edges)

    def __lt__(self, other):
        return True
