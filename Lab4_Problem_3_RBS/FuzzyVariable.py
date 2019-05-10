class FuzzyVariable:
    def __init__(self, name):
        self.name = name
        self.set = []

    def addSet(self, s):
        self.set.append(s)

    def membership(self, x):
        dict = []
        for s in self.set:
            dict.append([s.getLabel(), s.fuzzification(x)])
        return dict

    def getSetNumber(self):
        return self.set.__len__()

    def getSet(self):
        return self.set


