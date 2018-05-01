from copy import deepcopy
from filecmp import cmp


class Puzzle:
    def __init__(self, initial, final, x, y):
        self.__n = len(initial[0])
        self.__initial = initial
        self.__final = final
        self.__zerox = x
        self.__zeroy = y

    def get_initial(self):
        return self.__initial

    def get_final(self):
        return self.__final

    def get_n(self):
        return self.__n

    def get_zeroy(self):
        return self.__zeroy

    def get_zerox(self):
        return self.__zerox

    def __eq__(self, other):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__initial[i][j] != other.get_initial()[i][j]:
                    return False
        return True

    def is_solution(self):
        return self.__initial == self.__final

    def expand(self):
        dir = []
        ip = [-1, 0, 1, 0]
        jp = [0, -1, 0, 1]
        for k in range(4):
            if self.__zerox + ip[k] >= 0 and self.__zerox + ip[k] < self.__n and self.__zeroy + jp[
                k] >= 0 and self.__zeroy + jp[k] < self.__n:
                new_state = deepcopy(self.__initial)
                aux = new_state[self.__zerox][self.__zeroy]
                new_state[self.__zerox][self.__zeroy] = new_state[self.__zerox + ip[k]][self.__zeroy + jp[k]]
                new_state[self.__zerox + ip[k]][self.__zeroy + jp[k]] = aux

                new_zerox = self.__zerox + ip[k]
                new_zeroy = self.__zeroy + jp[k]
                dir.append(Puzzle(new_state, self.__final, new_zerox, new_zeroy))
        return dir

    def __cmp__(self, other):
        dif = 0
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__initial[i][j] != self.__final[i][j]:
                    dif += 1
        return cmp(dif, 0)

    def diferenta_pos(self):
        dif = 0
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__initial[i][j] != self.__final[i][j]:
                    dif += 1
        return dif

    def __lt__(self, other):
        return self.diferenta_pos() < other.diferenta_pos()

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self):
        s = ""
        for i in range(self.__n):
            for j in range(self.__n):
                s += str(self.__initial[i][j]) + " "
            s += "\n"
        return s
