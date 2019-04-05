#Unifinished
class Node(object):
    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightChild = None
        self.leftChild = None
        self.balance = 0

    def insert(self, data, parentNode):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)
        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)
        return parentNode

    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()
        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInOrder()

    def getMax(self):
        if not self.rightChild:
            return self.data
        else:
            self.rightChild.getMax()

    def getMin(self):
        if not self.leftChild:
            return self.data
        else:
            self.leftChild.getMin()

class balanceTree(object):
    def __init__(self):
        self.rootNote = None

    def insert(self, data):
        parentNode = self.rootNode

        if self.rootNode == None:
            parentNode = Node(data, None)
            self.rootNode = parentNode
        else:
            parentNode = self.rootNode.insert(data, self.rootNode)

        self.rebalanceTree(parentNode)

    def rebalanceTree(self, parentNode):
        self.setBalance(parentNode)

    def setBalance(self, node):
        node.balance = (self.height(node.rightChild) - self.height(node.leftChild))

    def height(self, node):
        if node = None:
            return -1
        else:
            return 1 + max(self.height(node.leftChild), self.height(node.rightChild))
