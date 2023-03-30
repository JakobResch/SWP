import random

class ListNode:

    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None

    def setPrevNode(self, node):
        self.prevNode = node

    def setNextNode(self, node):
        self.nextNode = node

    def getPrevNode(self):
        return self.prevNode

    def getNextNode(self):
        return self.nextNode

    def getValue(self):
        return self.value


class DoublyLinkedList:

    def __init__(self):
        self.firstNode = ListNode(None)
        self.lastNode = ListNode(None)
        self.firstNode.setNextNode(self.lastNode)
        self.lastNode.setPrevNode(self.firstNode)

    def getFirstNode(self):
         return self.firstNode.getNextNode().getElement()

    def getLastNode(self):
        return self.lastNode.getPrevNode()

    def addNode(self, value):
        if isinstance(value, int):
            newNode = ListNode(value)
            lastNode = self.getLastNode()
            lastNode.setNextNode(newNode)
            newNode.setPrevNode(lastNode)
            newNode.setNextNode(self.lastNode)
            self.lastNode.setPrevNode(newNode)

    def getLength(self, node=None, n=0):
        if node == None:
            node = self.firstNode
        if node.getNextNode() != None:
            node = node.getNextNode()
            n += 1
            return self.getLength(node, n)
        return n

    def printAllNodes(self):
        node = self.firstNode
        allNodes = '| '
        while node.getNextNode().value != None:
            node = node.getNextNode()
            allNodes += str(node.getValue()) + ' | '
        return allNodes

    def getNodeIndex(self, value, start=None, n=0):
        if start == None:
            start = self.firstNode
        if start.getNextNode() != None:
            if start.getNextNode().getValue() == value:
                return n
            start = start.getNextNode()
            n += 1
            return self.getNodeIndex(value, start, n)
        return None

    def getNodeByIndex(self, index):
        start = self.firstNode
        n = 0
        while start.getNextNode() != None:
            start = start.getNextNode()
            if n == index:
                return start.getValue()
            n += 1
        return None

    def deleteNode(self, value):
        start = self.firstNode

        while start.getNextNode() != None and value != start.getValue():
            if value == start.getNextNode().getValue():
                if start.getNextNode().getNextNode() != None:
                    start.setNextNode(start.getNextNode().getNextNode())
                    start.getNextNode().setPrevNode(start)
                else:
                    start.setNextNode(None)
                    break
            start = start.getNextNode()

    def findNode(self, value):
        start = self.firstNode
        while start.getNextNode() != None:
            if start.getNextNode().getValue() == value:
                return True
            start = start.getNextNode()
        return False

    def insertAfter(self, prevValue, value):
        node = self.firstNode.getNextNode()
        while node != None and node.getValue() != prevValue:
            node = node.getNextNode()

        newNode = ListNode(value)
        if node != None:
            nextNode = node.getNextNode()
            node.setNextNode(newNode)
            newNode.setNextNode(nextNode)
            newNode.setPrevNode(node)

    def insertBefore(self, nextValue, value):
        node = self.firstNode.getNextNode()
        while node != None and node.getValue() != nextValue:
            node = node.getNextNode()

        newNode = ListNode(value)
        if node != None:
            prevNode = node.getPrevNode()
            prevNode.setNextNode(newNode)
            newNode.setPrevNode(prevNode)
            newNode.setNextNode(node)
            node.setPrevNode(newNode)

if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    random_list = random.sample(range(0, 100), 10)
    node_val = random_list[5]
    for i in random_list:
        linked_list.addNode(i)

    print(linked_list.printAllNodes())
    print('First Value: ' + str(linked_list.getFirstNode().getValue()))
    print('Last Value: ' + str(linked_list.getLastNode().getValue()))
    print('Index: ' + str(linked_list.getNodeIndex(node_val)))
    print('Value: ' + str(linked_list.getNodeByIndex((linked_list.getNodeIndex(node_val)))))
    print('Länge: ' + str(linked_list.getLength()))
    print('Found Element %s: %s' % (node_val, str(linked_list.findNode(node_val))))
    print('Found Element %s: %s' % (99, str(linked_list.findNode(99))))
    linked_list.deleteNode(node_val)
    print(linked_list.printAllNodes())
    print('Länge: ' + str(linked_list.getLength()))
    prev = random_list[4]
    before = random_list[7]
    linked_list.insertAfter(prev, node_val)
    linked_list.insertBefore(before, node_val)
    print(linked_list.printAllNodes())
    print('Länge: ' + str(linked_list.getLength()))
    
    