from Controller import Controller
from Swarm import Swarm

class UI:
    def __init__(self, file):
        self.file = file
        data = self.readFromFile(file)
        self.prices = [50, 20, 20, 60, 10, 40, 50, 30, 30]
        self.greut = [12, 13, 10, 10, 20, 10, 10, 5, 15]
        self.nrP = int(data[0])
        self.maxParticle = int(data[1])
        self.minParticle = int(data[2])
        self.g = int(data[3])
        self.w = data[4]
        self.c1 = data[5]
        self.c2 = data[6]
        self.Pop = Swarm(self.minParticle, self.maxParticle, self.g, self.greut, self.prices, 100)
        self.Contrl = Controller(self.Pop, self.c1, self.c2, self.w)
        self.noIterations = int(data[7])

    def printMenu(self):
        s = '1.Run the algorithm. \n'
        s = s + '2.See the plot of the fitness variation. \n'
        s = s + '4.Exit'
        print(s)

    def run(self):
        keepRun = True
        while (keepRun):
            self.printMenu()
            ans = int(input())
            if ans == 1:
                print(self.Contrl.run(self.noIterations))
            elif ans == 2:
                print(self.Contrl.stat(self.noIterations))
            elif ans == 3:
                self.Contrl.ploting(self.noIterations)
            elif ans == 4:
                keepRun = False
            else:
                print("Not a valid option.")

    def readFromFile(self, file):
        with open(file)as f:
            return [float(x) for x in f]
