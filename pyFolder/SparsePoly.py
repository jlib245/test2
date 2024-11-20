from LinkedList import Node, LinkedList

# 다항식의 항을 나타내는 클래스
class Term:
    def __init__(self, expo, coef):
        self.expo = expo  # 지수
        self.coef = coef  # 계수

    def __str__(self):
        return f"{self.coef}x^{self.expo}"

# LinkedList를 상속받는 SparsePoly 클래스
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()  # LinkedList 초기화

    def getNode(self, pos):
        if pos < 0: 
            return None  # 잘못된 위치는 None 반환
        
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def insert(self, pos, elem):
        if pos < 0:
            raise IndexError("Position must be non-negative.")
        
        if pos == 0:  # 맨 앞에 삽입
            self.head = Node(elem, self.head)
            return

        # 이전 노드를 가져옴
        before = self.getNode(pos - 1)
        if before == None:  # 이전 노드가 없으면 예외 처리
            raise IndexError("Position out of bounds.")

        # 새 노드 생성 및 삽입
        new_node = Node(elem, before.link)
        before.link = new_node

    def addTerm(self, coef, expo):
        if coef == 0:
            return  # 계수가 0이면 추가하지 않음

        # 현재 노드를 순회하며 삽입 위치를 찾음
        node = self.head
        pos = 0
        while node != None and node.data.expo > expo:
            node = node.link
            pos += 1

        # 동일한 지수가 존재하면 계수를 더함
        if node != None and node.data.expo == expo:
            node.data.coef += coef
            if node.data.coef == 0:  # 계수가 0이 되면 해당 항 삭제
                self.delete(pos)
        else:
            # 새 항을 삽입
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
    
    # Big-O : O(n^2)
    def __add__(self, other):
        result = SparsePoly()

        # 첫 번째 다항식 항들을 결과에 추가
        node = self.head
        while node != None:
            term = node.data
            result.addTerm(term.coef, term.expo)
            node = node.link

        # 두 번째 다항식 항들을 결과에 추가
        node = other.head
        while node != None:
            term = node.data
            result.addTerm(term.coef, term.expo)
            node = node.link

        return result
    
    def __eq__(self, other):

        # 두 다항식을 순회하면서 비교
        node1 = self.head
        node2 = other.head

        while node1 != None and node2 != None:
            term1 = node1.data
            term2 = node2.data

            # 지수 또는 계수가 다르면 False
            if term1.expo != term2.expo or term1.coef != term2.coef:
                return False

            node1 = node1.link
            node2 = node2.link

        # 두 다항식이 모두 끝났으면 True, 아니면 False
        return node1 == None and node2 == None