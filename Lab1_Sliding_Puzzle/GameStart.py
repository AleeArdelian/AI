from UI import UI
from Controller import Controller
from Probem import Problem
from State import Puzzle

initialPuz = Puzzle()
finalPuz = Puzzle()
prob = Problem("puzzle_2", initialPuz, finalPuz)
ctrl = Controller(prob)

ui = UI(ctrl)
ui.menu()

