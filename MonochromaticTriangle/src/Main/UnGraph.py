class Graph:
    def __init__(self, filename):
        self.vertices = []
        self.edges = []
        self.init_file(filename)

    def init_file(self, filename):
        with open(filename, 'r') as file:
            self.vertices = file.readline().rstrip('\n').split(' ')
            self.edges = list(map(lambda line: list(line.rstrip('\n').split(' ')), file.readlines()))

    def __str__(self):
        return str(self.vertices) + "\n" + str(self.edges) + "\n" + str(self.out_bound(self.edges))
