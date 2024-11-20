ans = []
while 1 :
    try :
        n = int(input())
    except :
        break
    if n <= 1 :
        res = 1
    else :
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 3
        for i in range(3, n+1) :
            dp[i] = dp[i-2]*2 + dp[i-1]
        res = dp[n]
    ans.append(res)

print(*ans, sep='\n')