from TNode import TNode

class BST:
  def __init__(self):
    self.root = None
  def isEmpty(self) : return self.root == None
  def Add(self, value):
    newTNode = TNode(value)
    if self.isEmpty() :
      self.root = newTNode
    else :
      insert(self.root, newTNode)
  def Search(self, value) :
    check = search(self.root, value)
    if check :
      print("T\n")
    else:
      print("F\n")
  def Union(self,B) :
    C = makeUnion(self.root, B.root)
    return C
  def Difference(self, B) :
    C = makeDifference(self.root, B.root)
    return C
  def LevelSum(self, level) :
    sum = levelSum(self.root, 1, level)
    return sum
  def Preorder_Traverse(self) :
    print("전위 순회 : ")
    preorder(self.root)
    print("\n")
  def Inorder_Nth(self, N) :
    global count
    count = 0
    print("중위 순회" + str(N) +"번째 : ")
    inorder(self.root, N)

def makeDifference(A,B) :
  Aset=[]
  Bset=[]
  pickInorder(A,Aset)
  pickInorder(B,Bset)
  Cset = []
  for i in Aset :
    if i not in Bset :
      Cset.append(i)
  
  C = BST()
  for i in Cset :
    C.Add(i)
  
  return C

def levelSum(cur, curlevel ,level) :
  if cur == None :
    return 0
  
  if curlevel == level :
    return cur.value
  
  left = levelSum(cur.left, curlevel +1,level)
  right = levelSum(cur.right,curlevel+1,level)

  return left + right

def makeUnion(A,B):
  Aset=[]
  Bset=[]
  pickInorder(A,Aset)
  pickInorder(B,Bset)
  Cset = Aset
  for i in Bset :
    if i not in Cset :
      Cset.append(i)
  
  C = BST()
  for i in Cset :
    C.Add(i)
  
  return C


def search(cur, N) :
  if cur == None:
    return False
  elif cur.value == N:
    return True
  elif cur.value > N:
    return search(cur.left,N)
  elif cur.value < N:
    return search(cur.right,N)
       
def insert( cur, N):
  if (N.value < cur.value) :
    if cur.left is None :
      cur.left = N
      return True
    else :
      return insert(cur.left, N)
  elif (N.value > cur.value) :
    if cur.right is None :
      cur.right = N
      return True
    else :
      return insert(cur.right, N)
  else :
    return False

def pickInorder(cur, box):
  if cur is not None :
    pickInorder(cur.left, box)
    box.append(cur.value)
    pickInorder(cur.right, box)

def preorder(cur):
  if cur is not None :
    print(cur.value, end=' ')
    preorder(cur.left)
    preorder(cur.right)

def inorder(cur, N ):
  global count
  if cur is not None :
    inorder(cur.left, N)
    count = count + 1
    if count == N :
      print(cur.value)
    inorder(cur.right, N)

def inputNum(BST, string):
  s = string.split(' ')
  for i in s:
    if int(i) == 0:
      break
    BST.Add(int(i))

A = BST()
B = BST()

inputstr = input("입력 ")
inputNum(A, inputstr)
inputstr = input("입력 ")
inputNum(B, inputstr)

A.Search(14) #T
A.Search(13) #F
B.Search(-1) #T
B.Search(0) #F

C = A.Union(B)
D = A.Difference(B)

print(C.isEmpty()) #False
print(D.isEmpty()) #False
print(C.Difference(D).isEmpty()) #False

print(C.LevelSum(3))

C.Preorder_Traverse()
D.Preorder_Traverse()

print(C.Inorder_Nth(5))
