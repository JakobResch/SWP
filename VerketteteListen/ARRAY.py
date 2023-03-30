import random
import copy
from Arr_Decorator import decorator


class ArrayList:

    def __init__(self):
        self.list = [None]*5
        self.numElements = 0

    @decorator.getLastNode
    def getLastNode(self):
        return 'Last Element: '

    def addNode(self, element):
        if self.numElements >= len(self.list):
            newList = [None] * (2*len(self.list))
            for i in range(0,len(self.list)):
                newList[i] = self.list[i]
            self.list = newList
        self.list[self.numElements] = element
        self.numElements += 1
        return self.list

    @decorator.getLength
    def getLength(self):
        return 'Länge: '

    @decorator.printAllNodes
    def __str__(self):
        return self.list


    @decorator.getNodeIndex

    def getNodeIndex(self, elem,  n=0):
        return 'Index: '

    @decorator.getNodebByIndex
    def getNodebByIndex(self, index):
        return 'Element: '

    @decorator.deleteNode
    def deleteNode(self, index):
        return
    @decorator.findNode
    def findNode(self, elem):
        return 'Found Element '

    @decorator.add
    def insertAfter(self, prevElem, elem):
        pass


if __name__ == '__main__':
    Liste = ArrayList()
    randomlist = random.sample(range(0, 100), 10)
    elem = randomlist[5]
    for i in randomlist:
        Liste.addNode(i)

    print(Liste)
    Liste.getLastNode()
    Liste.getNodeIndex(elem)
    Liste.getNodebByIndex((Liste.getNodeIndex(elem)))
    Liste.getLength()
    Liste.findNode(elem)
    Liste.findNode(99)
    Liste.deleteNode(Liste.getNodeIndex(elem))
    print(Liste)
    Liste.getLength()
    prev = randomlist[4]
    Liste.insertAfter(prev, elem)
    print(Liste)
    Liste.getLength()
