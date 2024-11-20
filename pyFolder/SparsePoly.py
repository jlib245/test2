from LinkedList import *

class Term() :
    def __init__(self, expo, coef):
        self.expo = expo
        self.coef = coef

class SparsePoly(LinkedList) :
    def __init__(self):
        super().__init__()

    def getNode(self, coef, expo) :
        if expo < 0 : 
            return
        
        if coef == 0:
            return # 계수가 0인 항은 저장하지 않음

        # 올바른 위치(지수 순서)에 항을 삽입
        node = self.head
        pos = 0
        while node != None and node.data.expo > expo:
            node = node.link
            pos += 1

        # 동일한 지수가 이미 존재하면 계수만 업데이트
        if node != None and node.data.expo == expo:
            node.data.coef += coef
            if node.data.coef == 0:  # 계수가 0이 되면 삭제
                self.delete(pos)
        else:
            self.insert(pos, Term(expo, coef))  # 새로운 항 삽입

    def read(self) :
        while 1 :
            s = input("계수 차수 입력(종료:-1): ")
            if s == "-1" :
                break
            coef, expo = map(int, s.split())
            self.getNode(coef, expo)
    
    def display(self) :
        terms = []
        node = self.head
        while node != None:
            term = node.data
            terms.append(f"{term.coef}x^{term.expo}")
            node = node.link
        print(" + ".join(terms))

    
    def __add__(self, polyB):
        """
        두 다항식을 더한 결과를 반환.
        other: SparsePoly 객체
        """
        result = SparsePoly()
        node1 = self.head
        node2 = polyB.head

        while node1 is not None and node2 is not None:
            term1 = node1.data
            term2 = node2.data

            if term1.expo > term2.expo:
                result.addTerm(term1.coef, term1.expo)
                node1 = node1.link
            elif term1.expo < term2.expo:
                result.addTerm(term2.coef, term2.expo)
                node2 = node2.link
            else:  # 같은 지수일 경우 계수를 더함
                result.addTerm(term1.coef + term2.coef, term1.expo)
                node1 = node1.link
                node2 = node2.link

        # 남아있는 항 추가
        while node1 is not None:
            term1 = node1.data
            result.addTerm(term1.coef, term1.expo)
            node1 = node1.link

        while node2 is not None:
            term2 = node2.data
            result.addTerm(term2.coef, term2.expo)
            node2 = node2.link

        return result
        
    def __eq__(self, polyB):
        """
        두 다항식이 동일한지 비교.
        other: SparsePoly 객체
        반환: 동일하면 True, 다르면 False
        """
        node1 = self.head
        node2 = polyB.head

        while node1 is not None and node2 is not None:
            term1 = node1.data
            term2 = node2.data

            # 지수와 계수가 동일하지 않으면 False
            if term1.expo != term2.expo or term1.coef != term2.coef:
                return False

            node1 = node1.link
            node2 = node2.link

        # 두 다항식 중 하나가 끝나지 않았다면 False
        return node1 == None and node2 == None
    
a = SparsePoly()
a.read()
a.display()