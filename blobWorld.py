import random

class Blob:
    def __init__(self,friendliness,greediness,productivity,motivation,energy):
        self.friendliness = friendliness
        self.greediness = greediness
        self.productivity = productivity
        self.motivation = motivation
        self.energy = energy
        self.days = 14


    def setEnergy(self,delta):
        #write code for decreasing/increasing energy by delta
        self.energy = delta

        if(self.energy > 20):
            self.energy = 20

        if(self.energy < 0):
            self.energy = 0

    
    def getEnergy(self):
        return self.energy


    def setMotivation(self,delta):
       #write code for decreasing/increasing motivation by delta
        self.motivation += delta

        if(self.motivation > 10):
            self.motivation = 10

        if(self.motivation < 0):
            self.motivation = 0

    
    def getMotivation(self):
        return self.motivation

    
    def setProductivity(self,delta):
        #write code for decreasing/increasing productivity by delta
        self.productivity += delta

        self.productivity += delta

        if(self.productivity > 3):
            self.productivity = 3

        if(self.productivity < 1):
            self.productivity = 1


    def getProductivity(self):
        return self.productivity


    def reproduce(self):
        #write code for altering the parameters when reproducing
        #also make a new blob as reproduction produces 2 blobs
        if(self.greediness < 6 and self.energy >= 10):
            self.setEnergy(self.energy // 2)
            return Blob(self.friendliness,self.greediness,self.productivity,self.motivation,self.energy)

        elif(self.greediness >= 6 and self.greediness < 9 and self.energy >= 12):
            self.setEnergy(self.energy // 2)
            return Blob(self.friendliness,self.greediness,self.productivity,self.motivation,self.energy)

        elif(self.greediness >= 9 and self.greediness <= 10 and self.energy >= 14):
            self.setEnergy(self.energy // 2)
            return Blob(self.friendliness,self.greediness,self.productivity,self.motivation,self.energy)

        else:
            return None



    
    def die(self):
        #if the energy goes 0 than the blob dies
	   # del self
       pass

    def hunt(self):
        #put if else statements here to determine which tree to work upon
        if(self.motivation <= 4):
            return banana_tree.hunt(self)

        elif(self.motivation >= 5 and self.motivation <= 7):
            return apple_tree.hunt(self)

        else:
            return mango_tree.hunt(self)

    def hunt2(self):
        #put if else statements here to determine which tree to work upon
        if(self.motivation >= 5 and self.motivation <= 7):
            return apple_tree.hunt(self)

        else:
            return mango_tree.hunt(self)


    def borrow(self,blob):
        #code for borrowing(the blob paramter denotes the blob from whom energy is borrowed)
        pass

        
class Tree:

    def __init__(self,type, increaseForProdOne, increaseForProdTwo, increaseForProdThree, increaseMotivation):
        self.type = type
        self.increaseForProdOne = increaseForProdOne
        self.increaseForProdTwo = increaseForProdTwo
        self.increaseForProdThree = increaseForProdThree
        self.increaseMotivation = increaseMotivation

    def hunt(self,Blob):
        #code to alter the energy etc levels of the blob if he works on this tree
        Blob.setMotivation(self.increaseMotivation)
        if(Blob.getProductivity() == 1):
            Blob.setEnergy(Blob.energy + self.increaseForProdOne)
            return self.increaseForProdOne

        elif(Blob.getProductivity == 2):
            Blob.setEnergy(Blob.energy + self.increaseForProdTwo)
            return self.increaseForProdTwo

        else:
            Blob.setEnergy(Blob.energy + self.increaseForProdThree)
            return self.increaseForProdThree


    def setIncreaseMotivation(self, motivation):
        self.increaseMotivation = motivation


class Banana(Tree):
    #code for banana
    def __init__(self):
        Tree.__init__(self,"banana", 1, 2, 4, 2)


class Apple(Tree):
    #code for apple
    def __init__(self):
        Tree.__init__(self,"apple", 2, 4, 6, 1)

    def hunt(self, Blob):
        generateMotivation = random.randint(0,2)
        if(generateMotivation == 1):
            Blob.setMotivation(-1)
        else:
            Blob.setMotivation(1)

        super().hunt(Blob)


class Mango(Tree):
    #code for mango
    def __init__(self):
        Tree.__init__(self,"mango", 4, 8, 8, -2)


class Day:
    #not sure if this is needed
    pass


banana_tree = Banana()
apple_tree = Apple()
mango_tree = Mango()
