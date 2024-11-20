from SparsePoly import SparsePoly
# SparsePoly 인스턴스 생성
A = SparsePoly()
B = SparsePoly()

A.read()
B.read()

A.display("A =")
B.display("B =")
(A+B).display("A+B =")

'''
3 12
2 8
1 0
-1 -1
8 12
-3 10
10 6
-1 -1

'''