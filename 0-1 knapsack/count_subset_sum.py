def countOfSubsetSum(arr,n,summ):
    dp = [[-1 for i in range(summ+1)] for j in range(n+1)]

    for i in range(summ+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,summ+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][summ]

arr = list(map(int,input().split()))
n = len(arr)
summ = int(input())
print(countOfSubsetSum(arr,n,summ))

# Find number of subset with given sum
# Input: arr[] = {1, 2, 3, 3}, X = 6
# Output: 3
# All the possible subsets are {1, 2, 3},
# {1, 2, 3} and {3, 3}