from Algorithm import Algorithm


class Application:
    def printMenu(self):
        print('1. See minimum')
        print('2. Statistics')

    def main(self):
        alg = Algorithm()
        running = True
        while running:
            self.printMenu()
            choice = int(input("\n Choose: "))
            if choice == 1:
                alg.displayRun()
            elif choice == 2:
                alg.statistics()
            else:
                running = False


a = Application()
a.main()
