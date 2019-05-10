class FuzzySet:
    def __init__(self, label, values):
        self.label = label
        self.values = values
        self.a = None
        self.b = None
        self.c = None
        self.setValues()

    def setValues(self):
        self.a = self.values[0]
        self.b = self.values[1]
        self.c = self.values[2]

    def fuzzification(self, x):
        return max(0, min((x - self.a) / (self.b - self.a), 1, (self.c - x) / (self.c - self.b)))

    def getCenter(self):
        return self.b

    def getLabel(self):
        return self.label