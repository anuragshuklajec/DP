def knapsack_iter(wt,val,W,n,dp):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j ==0:
                dp[i][j] = 0

    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


wt = list(map(int,input().split()))
val = list(map(int,input().split()))
W = int(input())
n = len(wt)
dp = [[-1 for i in range(W+1)] for j in range(n+1)]
print(knapsack_iter(wt,val,W,n,dp))