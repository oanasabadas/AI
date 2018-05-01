from queue import PriorityQueue


class PuzzleCtrl:
    def __init__(self, puzzle):
        self.__puzzle = puzzle

    def get_puzzle(self):
        return self.__puzzle

    def bfs(self):
        # iteratii = 0
        visited = {}
        queue = []
        solutions = []
        init = [self.__puzzle]
        queue.append(init)
        while queue != []:
            current = queue[0]
            queue = queue[1:]
            # iteratii += 1
            # print(iteratii)
            if current[-1] not in visited.keys():
                visited[current[-1]] = True
            if current[-1].is_solution():
                solutions.append(current)
                return solutions
            for e in current[-1].expand():
                if current[-1] not in visited.keys():

                    current = current + [e]
                    if current[-1].is_solution():
                        solutions.append(current)
                        return solutions
                    visited[current[-1]] = True
                    queue.append(current)
                    current = current[:-1]
        # print(iteratii)
        return solutions

    def gbfs(self):
        visited = {}
        iteratii = 0
        queue = PriorityQueue()
        solutions = []
        init = [self.__puzzle]
        queue.put(init)
        while queue != []:
            current = queue.get()
            iteratii += 1
            print(iteratii)
            if current[-1] not in visited.keys():
                visited[current[-1]] = True
            if current[-1].is_solution():
                solutions.append(current)
                return solutions
            for e in current[-1].expand():
                if e not in visited.keys():
                    current = current + [e]
                    if current[-1].is_solution():
                        solutions.append(current)
                        return solutions
                    visited[current[-1]] = True
                    queue.put(current)
                    current = current[:-1]
        print(iteratii)
        return solutions
