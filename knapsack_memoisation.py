def knapsack_memo(wt,val,W,n,dp):
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    else:
        if wt[n-1] <= W:
            dp[n][W] = max(val[n-1] + knapsack_memo(wt,val,W-wt[n-1],n-1,dp),knapsack_memo(wt,val,W,n-1,dp))

        else:
            dp[n][W] = knapsack_memo(wt,val,W,n-1,dp)
        return dp[n][W]


wt = list(map(int,input().split()))
val = list(map(int,input().split()))
W =int(input())
n = len(wt)
dp = [[-1 for i in range(n+1)] for j in range(W+1)]
print(knapsack_memo(wt,val,W,n,dp))