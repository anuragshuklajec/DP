def subset_sum(arr,sum,n):

    dp = [[-1 for i in range(sum + 1)] for j in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = True
    for j in range(1,sum+1):
        dp[0][j] = False

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]

arr = list(map(int,input().split()))
sum = int(input())
n = len(arr)

print(subset_sum(arr,sum,n))

# test case
# arr = 2 3 7 8 10
# sum = 11
# is subset present whose sum equals 11