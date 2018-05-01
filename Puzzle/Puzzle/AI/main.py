from AI.Controller.PuzzleCtrl import PuzzleCtrl
from AI.Domain.Puzzle import Puzzle
from AI.UI.Console import Console



def main1():

    init = open("C:\\Users\\oana\\PyCharm\\Puzzle\\AI\\Resources\\init.txt").read()
    init = [item.split() for item in init.split("\n")[:]]

    fin = open("C:\\Users\\oana\\PyCharm\\Puzzle\\AI\\Resources\\final.txt").read()
    fin = [item.split() for item in fin.split("\n")[:]]

    p2=Puzzle(init,fin,2,2)


    ctrl=PuzzleCtrl(p2)
    r=ctrl.gbfs()
    for x in r:
        for xx in x:
            print(xx)



def main():
    init = open("init.txt").read()
    init = [item.split() for item in init.split("\n")[:]]

    fin = open("fin.txt").read()
    fin = [item.split() for item in fin.split("\n")[:]]

    p2=Puzzle(init,fin,2,1)
    ctrl=PuzzleCtrl(p2)
    cons=Console(ctrl)
    cons.run()

main()