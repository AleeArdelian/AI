def _print_menu():
    print("\n\tPSO for McCormick Function\n")
    print(" 1. Find minimum point")
    print(" 2. See the swarm")
    print(" 3. Statistics")
    print(" 0. Exit\n")


class UI:

    def __init__(self, alg):
        self._alg = alg

    def start(self):
        running = True
        while running:
            _print_menu()
            choice = int(input("Choice: "))
            if choice == 1:
                self._alg.run()
            elif choice == 2:
                print(self._alg.swarm)
            elif choice == 3:
                self._alg.stats()
            else:
                running = False
