import sys, math
input = sys.stdin.readline

N = int(input())
d = []
for i in range(N):
    x, r = map(int, input().split())
    d.append((x-r, x, r, i))
    d.append((x+r, x, r, i))
d.sort()

def check(x : int, y : int) -> bool :
    # 같은 번호의 원이라면 True
    if d[x][3] == d[y][3]:
        return True
    
    # 다른 번호의 원인데 x축에서 만날 시 False
    if d[x][0] == d[y][0] :
        return False

    # 위 두 조건을 전부 만족했을 시 중심에 따라 조건 분기
    dist = math.sqrt((d[x][1]-d[y][1])**2 + (d[x][1]-d[y][1])**2)
    
    

    

for i in range(1, 2*N-1):
    if not (check(i-1, i) and check(i, i+1)) :
        print("NO")
        break
else :
    print("YES")