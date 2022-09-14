def equal_sum_partition(arr,n):
    summ = sum(arr)

    if summ%2!=0:
        return False

    newSum = summ//2

    dp = [[-1 for i in range(newSum+1)] for j in range(n+1)]

    for i in range(newSum+1):
        dp[0][i] = False

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,newSum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][newSum]

arr = list(map(int,input().split()))
n = len(arr)
print(equal_sum_partition(arr,n))




