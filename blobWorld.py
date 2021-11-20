class Blob:
    def __init__(self,friendliness,greediness,productivity,motivation,energy):
        self.friendliness = friendliness
        self.greediness = greediness
        self.productivity = productivity
        self.motivation = motivation
        self.energy = energy

    def setEnergy(self,delta):
        #write code for decreasing/increasing energy by delta
    
    def getEnergy(self):
        return self.energy

    def setMotivation(self,delta):
       #write code for decreasing/increasing motivation by delta
    
    def getMotivation(self):
        return self.motivation
    
    def setProductivity(self,delta):
        #write code for decreasing/increasing productivity by delta

    def getProductivity(self):
        return self.productivity

    def reproduce(self):
        #write code for altering the parameters when reproducing
        #also make a new blob as reproduction produces 2 blobs

    def die(self):
        #if the energy goes 0 than the blob dies
        del self

    def hunt(self):
        #put if else statements here to determine which tree to work upon

    def borrow(self,blob):
        #code for borrowing(the blob paramter denotes the blob from whom energy is borrowed)

        
class Tree:
    def __init__(self,type):
        self.type = type

    def hunt(self,Blob):
        #code to alter the energy etc levels of the blob if he works on this tree

class Banana(Tree):
    #code for banana
    def __init__(self):
        Tree.__init__(self,"banana")

class Apple(Tree):
    #code for apple
    def __init__(self):
        Tree.__init__(self,"apple")

class Mango(Tree):
    #code for mango
    def __init__(self):
        Tree.__init__(self,"mango")


class Day:
    #not sure if this is needed