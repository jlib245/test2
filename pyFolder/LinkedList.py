from Node import Node

class LinkedList :
    def __init__(self) :
        self.head = None
    
    def isEmpty(self) :
        return self.head==None
    
    def isFull(self) :
        return False

    def getNode(self, pos) :
        if pos < 0 : 
            return False
        
        node = self.head
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None :
            return None
        return node.data

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :
            if self.head != None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link