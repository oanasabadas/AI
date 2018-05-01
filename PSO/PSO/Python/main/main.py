from Python.main.Controller import Controller
from Python.main.Particle import Particle
from Python.main.Problem import Problem
from Python.main.Swarm import Swarm


def main():
    problem = Problem("graph.txt")
    p = Particle(problem.edges, problem.vertices)
    swarm = Swarm(10, problem.edges, problem.vertices, 4)
    # print(swarm)
    # ctrl = Controller(swarm, 0.2, 0.5, 10)
    # print(ctrl)
    # ctrl.iteration()
    ctrl = Controller(swarm, 9.2, 5.5, 1.0)
    for i in range(10):
        P = ctrl.iteration()
        ctrl = Controller(P, 9.2, 5.5, 1.0 / (i + 1))

    # print the best individual
    print(P)
    best = 0
    for i in range(P.size):
        if (P.values[i].fitness < P.values[best].fitness):
            best = i


    fitnessOptim = P.values[best].fitness
    individualOptim = P.values[best].position
    print(fitnessOptim)
    print(individualOptim)


if __name__ == '__main__':
    main()
