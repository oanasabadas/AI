import matplotlib.pyplot

from src.Main.UnGraph import Graph
from src.Main.algorithm import Algorithm


def main():
    problem = Graph("graph.txt")
    a = Algorithm(problem, 0.1, 40)
    for i in range(1000):
        a.iteration()
    ps = a.population
    lis = ps.values
    graded = [(x.fitness(), x) for x in lis]
    graded = sorted(graded, reverse=True)
    result = graded[0]
    fitness = result[0]
    res = graded[len(graded) - 1]
    fit = res[0]
    ind = res[1]
    print(fit)
    print(ind)
    return [fit]


best_ind = []
for i in range(30):
    best_ind = best_ind + main()
print(best_ind)
matplotlib.pyplot.plot(range(30), best_ind)
matplotlib.pyplot.show()

