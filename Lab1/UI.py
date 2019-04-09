
class UI:
    def __init__(self, controller):
        self._contr = controller

    @staticmethod
    def subMenu():
        string = ''
        string += '\t Select board\n'
        string += '\t Press 0 to exit\n'
        string += '\t Press 1 to solve using an uninformed search method / bfs \n'
        string += '\t Press 2 to solve using an informed search method / gbfs \n'
        print(string)

    def uiBFS(self):
        steps = self._contr.BFS()
        if steps is None:
            print("Cannot reach configuration!")
        else:
            for p in steps:
                p.printTable()

    def uiGBFS(self):
        steps = self._contr.GBFS()
        if steps is None:
            print("Cannot reach configuration!")
        else:
            for p in steps:
                p.printTable()

    def menu(self):
        flag = True
        while flag:
            self.subMenu()
            x = int(input("Choose: "))
            if x == 0:
                flag = False
            elif x == 1:
                self.uiBFS()
            elif x == 2:
                self.uiGBFS()
            break
