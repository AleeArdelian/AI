from random import randint, random
from operator import add
import math
import copy
import statistics
from matplotlib import pyplot as plt

class particle:
    """ The class that implements a particle """
    def __init__(self, l,k, g, grams,prices):
      
        self.grams=grams
        self.prices=prices
        self.limit=g
        self.min=l
        self.max=k
    
        self._pozition = [ (randint(0,1)) for x in range(len(grams))]
        self.evaluate()
        self.velocity = [ 0 for i in range(len(self._pozition))]
        
        #the memory of that particle
        self._bestPozition=copy.deepcopy(self._pozition)
        self._bestFitness=self._fitness
        
 
            
    def fit(self,pozition,price,grams,limit,g,l):
        n=len(pozition)
        f=0
        for i in range(0,len(pozition)):
            f+=pozition[i]*price[i]
        ones=0
        suma=0
            
        for i in range(0,len(pozition)):
            suma+=grams[i]*pozition[i]
        
            ones=ones+pozition[i]
        penalization=0
        if ones>g: 
            penalization=(ones-g)*500
        if ones<l:
            penalization=(l-ones)*500
     
        return (f-((limit*abs(suma-limit)))-penalization)
            
        

    def evaluate(self):
        """ evaluates the particle """
        self._fitness=self.fit(self._pozition,self.prices,self.grams,self.limit,self.max,self.min)
    def evaluation(self):
        self._pozition=self.evaluate()
    @property
    def pozition(self):
        """ getter for pozition """
        return self._pozition

    @property
    def fitness(self):
        """ getter for fitness """
        return self._fitness

    @property
    def bestPozition(self):
        """ getter for best pozition """
        return self._bestPozition

    @property
    def bestFitness(self):
        """getter for best fitness """
        return self._bestFitness
    
    @pozition.setter
    def pozition(self, newPozition):
        self._pozition=newPozition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self._fitness>self._bestFitness):
            self._bestPozition = self._pozition
            self._bestFitness  = self._fitness
    def update(self):
        if (self._fitness>self._bestFitness):
            self._bestPozition = self._pozition
            self._bestFitness  = self._fitness
    def __str__(self):
        stri=""
        for i in self._pozition:
            stri+=str(i)
        return stri
    
class Population:
    def __init__(self,l,k,g,grams,prices,count):
        self.l=l
        self.k=k
        self.g=g
        self.grams=grams
        self.prices=prices
        self.count=count
        self.population=[ particle( l,k, g, grams,prices) for x in range(count) ]
    def getPopulation(self):
        return self.population

    def selectNeighbors(self,nsize):
        if (nsize>len(self.population)):
            nsize=len(self.population)

        neighbors=[]
        for i in range(len(self.population)):
            localNeighbor=[]
            for j in range(nsize):
                x=randint(0, len(self.population)-1)
                while (x in localNeighbor):
                    x=randint(0, len(self.population)-1)
                localNeighbor.append(x)
            neighbors.append(copy.deepcopy(localNeighbor))
        return neighbors
    def newPopulation(self):
        self.population=[ particle( self.l,self.k, self.g, self.grams,self.prices) for x in range(self.count) ]

class controller:
    def __init__(self,pop,c1,c2,w):
        self._population=pop
        self.c1=c1
        self.c2=c2
        self.w=w
    def iteration(self,pop,neighbors,c1,c2,w):
        bestNeighbors=[]
        #determine the best neighbor for each particle
        for i in range(len(pop)):
            bestNeighbors.append(neighbors[i][0])
            for j in range(1,len(neighbors[i])):
                if (pop[bestNeighbors[i]]._fitness<pop[neighbors[i][j]]._fitness):
                    bestNeighbors[i]=neighbors[i][j]
                    
        #update the velocity for each particle
        for i in range(len(pop)):
            for j in range(len(pop[0].velocity)):
                newVelocity = w * pop[i].velocity[j]
                newVelocity = newVelocity + c1*random()*(pop[bestNeighbors[i]].pozition[j]-pop[i].pozition[j])    
                newVelocity = newVelocity + c2*random()*(pop[i].bestPozition[j]-pop[i].pozition[j])
                pop[i].velocity[j]=newVelocity
                
                
        
        #update the pozition for each particle
        for i in range(len(pop)):
            newPozition=[]
            for j in range(len(pop[0].velocity)):
                x=self.sigmoid( pop[i].velocity[j])
                if x<=0.5:
                    newPozition.append(0)
                else:
                    newPozition.append(1)
            pop[i]._pozition=newPozition
            pop[i].evaluate()
            pop[i].update()
            
        return pop
    
    
    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))          
    
    def run(self,noIterations):
        P=self._population.getPopulation()
        neighborhoods=self._population.selectNeighbors(5)
        for i in range(noIterations):
            P = self.iteration(P, neighborhoods, self.c1,self.c2, self.w)
        
        best = 0
        for i in range(1, len(P)):
        
        
            if (P[i]._fitness>P[best]._fitness):
                best = i

            fitnessOptim=P[best]._fitness
        a=P[best]._pozition
        b=fitnessOptim
        self._population.newPopulation()
        return(a,b)
    def runForPlot(self,noIterations):
        P=self._population.getPopulation()
        neighborhoods=self._population.selectNeighbors(5)
        for i in range(noIterations):
            P = self.iteration(P, neighborhoods, self.c1,self.c2, self.w)
        
        Finesses=[]
        for i in range(1, len(P)):
            Finesses.append(P[i]._fitness)
        return Finesses   
        
    def  stat(self,noIterations):
        minValues=[self.run(noIterations)[1] for x in range(30)]
        return statistics.mean(minValues),statistics.stdev(minValues)
    def ploting(self,noIterations):
        values=self.runForPlot(noIterations)
        plt.plot(values)
        plt.show()
class UI:
    def __init__(self,file):
        self.file=file
        data=self.readFromFile(file)
        self.prices=[10,20,30,40,50,40,50]
        self.greut= [12,13,10,10,20,10,10]
        self.nrP=int(data[0])
        self.maxParticle=int(data[1])
        self.minParticle=int(data[2])
        self.g=int(data[3])
        self.w=data[4]
        self.c1=data[5]
        self.c2=data[6]
        self.Pop=Population(self.minParticle,self.maxParticle,self.g,self.greut,self.prices,100)
        self.Contrl=controller(self.Pop,self.c1,self.c2,self.w)
        self.noIterations=int(data[7])
    def printMenu(self):
        
        s='1.Run the algorithm. \n'
        
        s=s+'2.Do the test and see the average and the standard deviation. \n'
        s=s+'3.See the plot of the fitness variation.'
        s=s+'4.Exit'
        print(s)
    def run(self):
        keepRun=True
        while(keepRun):
            self.printMenu()
            ans=input()
            if ans==1:
                print(self.Contrl.run(self.noIterations))
            elif ans==2:
                print(self.Contrl.stat(self.noIterations))
            elif ans==3:
                self.Contrl.ploting(self.noIterations)
            elif ans==4:
                keepRun=False
            else:
                print("Not a valid option.")
    def readFromFile(self,file):   
        with open(file)as f:
            return[float(x) for x in f]
         
"""
def main():
    #PARAMETERS:
    
    #number of particles
    noParticles = 100
    #individual size
    maxParticle = 4
    #the boundries of the search interval
    minParticle=2
    
    g=20
    prices=[10,20,30,40,50,40,50]
    greut= [12,13,10,10,20,10,10]
    #specific parameters for PSO
    w=1.0
    c1=1.0
    c2=2.5
    sizeOfNeighborhood=5
    P = Population(minParticle,maxParticle,g,greut,prices,100)
    A= controller(P)
    A.run(100)
""" 
    
ui=UI("Dates.txt")
ui.run()

