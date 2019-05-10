from FuzzySet import FuzzySet
from FuzzyVariable import FuzzyVariable


class UI:
    def __init__(self, file, params):
        self.file = file
        self.params = params
        self.capacity = None
        self.texture = None
        self.cycle = None
        self.textureValue =None
        self.capacityValue = None
        self.rules = []
        self.readTexture()

    def printMenu(self):
        s = '1. See the texture value \n'
        s = s + '2. See the capacity value \n'
        s = s + '3. See cycle type value \n'
        s = s + '4. See rules \n'
        s = s + '5. See inferences \n'
        print(s)

    def run(self):
        file = open("output.out", "w")

        print('Texture membership for: ', self.textureValue)
        print(self.texture.membership(self.textureValue))
        file.write('Texture membership for: ' + str(self.textureValue))
        file.write(str(self.texture.membership(self.textureValue)) + '\n')

        print('Capacity membership for: ', self.capacityValue)
        print(self.capacity.membership(self.capacityValue))
        file.write('Capacity membership for: ' + str(self.capacityValue))
        file.write(str(self.capacity.membership(self.capacityValue)) + '\n')

        print('Rules: ')
        print(self.rules)
        file.write('Rules: ')
        file.write(str(self.rules)+ '\n')

        print('Inference: ')
        print(self.inference())
        file.write('Inference: ')
        file.write(str(self.inference()) + '\n')

        print('Agregate: ')
        print(self.aggregate(self.inference()))
        file.write('Agregate: ')
        file.write(str(self.aggregate(self.inference())) + '\n')

        print('Deffuzify value: ')
        defuz = self.defuzzify(self.aggregate(self.inference()), self.cycle)
        print(defuz)
        file.write('Deffuzify value: ')
        file.write(str(defuz) + '\n')

        print('Recommended wash cycle: ')
        maxim, label = self.recomended(self.cycle.membership(defuz))
        print('Max value: ', maxim, 'Cycle power: ', label)
        file.write('Recommended wash cycle: ')
        file.write('Max value: ' + str(maxim) + 'Cycle power: ' + str(label) + '\n')

    def inference(self):
        inferences = {}
        textureList = self.texture.membership(self.textureValue)
        capacityList = self.capacity.membership(self.capacityValue)
        for t in range(0, len(textureList)):
            for c in range(0, len(capacityList)):
                label = self.rules[t][c]
                if label in inferences.keys():
                    inferences[label].append(min(textureList[t][1], capacityList[c][1]))
                else:
                    inferences[label] = [min(textureList[t][1], capacityList[c][1])]
        return inferences

    def aggregate(self, inferences):
        aggregated = [max(inferences[x]) for x in inferences]
        return aggregated

    def defuzzify(self, aggregate, cycle):
        s1 = 0.0
        s2 = 0.0
        centers = cycle.getSet()
        for i in range(len(aggregate)):
            s1 += aggregate[i] * centers[i].getCenter()
            s2 += aggregate[i]
        return s1 / s2

    def recomended(self, cy):
        maxim = -10000
        label = None
        for x in cy:
            if maxim < x[1]:
                maxim = x[1]
                label = x[0]
        return maxim, label

    def readTexture(self):
        with open(self.params) as g:
            line = g.readline().strip('\n').split(' ')
            self.textureValue = float(line[0])
            self.capacityValue = float(line[1])
        with open(self.file) as f:
            line = f.readline().strip('\n').split(',')
            self.texture = FuzzyVariable(line[0])
            self.capacity = FuzzyVariable(line[1])
            self.cycle = FuzzyVariable(line[2])
            for x in range(4):
                line = f.readline().strip('\n').split(',')
                values = [float(line[1]), float(line[2]), float(line[3])]
                set = FuzzySet(line[0], values)
                self.texture.addSet(set)
            for x in range(3):
                line = f.readline().strip('\n').split(',')
                values = [float(line[1]), float(line[2]), float(line[3])]
                set = FuzzySet(line[0], values)
                self.capacity.addSet(set)
            for x in range(4):
                line = f.readline().strip('\n').split(',')
                values = [float(line[1]), float(line[2]), float(line[3])]
                set = FuzzySet(line[0], values)
                self.cycle.addSet(set)
            for x in range(self.texture.getSetNumber()):
                line = f.readline().strip('\n').split(',')
                self.rules.append([])
                for y in range(self.capacity.getSetNumber()):
                    self.rules[x].append(line[y])



