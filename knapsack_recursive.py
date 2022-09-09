def knapsack(wt,val,W,n):
    if len(wt) == 0 or W == 0:
        return 0

    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt,val,W-wt[n-1],n-1), knapsack(wt,val,W,n-1))
    else:
        return knapsack(wt,val,W,n-1)



wt = list(map(int,input().split()))
val = list(map(int,input().split()))
W = int(input())
n = len(wt)
print(knapsack(wt,val,W,n))