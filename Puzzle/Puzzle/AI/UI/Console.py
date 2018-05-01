import time

from AI.Controller.PuzzleCtrl import PuzzleCtrl
from AI.Domain.Puzzle import Puzzle


class Console:
    def __init__(self,c):
        self.__ctrl = c

    def print_menu(self):
        s = ''
        s += "0. Exit\n"
        s += "1. BFS\n"
        s += "2. GBFS\n"
        s += "3. Current game\n"
        print(s)

    def game_ui(self):
        print(self.__ctrl.get_puzzle())

    def bfs_ui(self):
        start_time = time.time()
        r=self.__ctrl.bfs()
        for x in r:
            for xx in x:
                print(xx)

        print("--- %s seconds ---" % (time.time() - start_time))

    def gbfs_ui(self):
        start_time = time.time()
        r=self.__ctrl.gbfs()
        for x in r:
            for xx in x:
                print(xx)

        print("--- %s seconds ---" % (time.time() - start_time))

    def run(self):
        var = True
        self.print_menu()
        while var:

            cmd = int(input("Option: "))
            if cmd == 0:
                var = False
            elif cmd == 1:
                 self.bfs_ui()
            elif cmd == 2:
                 self.gbfs_ui()
            elif cmd == 3:
                self.game_ui()




