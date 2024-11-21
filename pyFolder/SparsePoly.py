from LinkedList import Node, LinkedList

class Term:
    def __init__(self, expo, coef):
        self.expo = expo  # 지수
        self.coef = coef  # 계수

    def __str__(self):
        return f"{self.coef}x^{self.expo}"

# LinkedList를 상속
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()  

    def getNode(self, pos):
        if pos < 0: 
            return None  
        
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def insert(self, pos, elem):
        if pos < 0:
            raise IndexError("Position must be non-negative.")
        
        if pos == 0: 
            self.head = Node(elem, self.head)
            return

        before = self.getNode(pos - 1)
        if before == None:  
            return

        new_node = Node(elem, before.link)
        before.link = new_node

    def addTerm(self, coef, expo):
        if coef == 0:
            return  

        node = self.head
        pos = 0
        while node != None and node.data.expo > expo:
            node = node.link
            pos += 1

        if node != None and node.data.expo == expo:
            node.data.coef += coef
            if node.data.coef == 0:  
                self.delete(pos)
        else:
            self.insert(pos, Term(expo, coef))

    def evaluate(self, x):
        result = 0
        node = self.head
        while node != None:
            term = node.data
            result += term.coef * (x ** term.expo)
            node = node.link
        return result

    def read(self):
        while 1 :
            coef, expo = map(float, input("계수 차수 입력 (종료 : -1) : ").split())
            expo = int(expo)
            if coef == expo == -1 :
                break
            self.addTerm(coef, expo)

        self.display("입력 다항식 :")


    def display(self, s = ""):
        terms = []
        node = self.head
        while node != None:
            terms.append(str(node.data))
            node = node.link
        print(s, end=' ')
        print(" + ".join(terms) if terms else "0")
    
    # Big-O : O(m^2)
    def __add__(self, other):
        result = SparsePoly()

        node = self.head
        while node != None:
            term = node.data
            result.addTerm(term.coef, term.expo)
            node = node.link

        node = other.head
        while node != None:
            term = node.data
            result.addTerm(term.coef, term.expo)
            node = node.link

        return result
    
    def __eq__(self, other):

        node1 = self.head
        node2 = other.head

        while node1 != None and node2 != None:
            term1 = node1.data
            term2 = node2.data

            if term1.expo != term2.expo or term1.coef != term2.coef:
                return False

            node1 = node1.link
            node2 = node2.link

        return node1 == None and node2 == None
    
    def degree(self) :
        return self.head.data.expo
    
    def coef(self) :
        terms = []
        node = self.head
        while node != None:
            terms.append(node.data.coef)
            node = node.link

        return terms