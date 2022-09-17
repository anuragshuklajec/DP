def target_sum(arr,n,target):
    summ = sum(arr)
    newSum = (target+summ)//2

    dp = [[-1 for i in range(newSum+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,newSum+1):
        dp[0][i] = False

    for i in range(1,n+1):
        for j in range(1,newSum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][newSum]


arr = list(map(int,input().split()))
n = len(arr)
target = int(input())
print(target_sum(arr,n,target))


# problem similar to number of subset with difference

# Target Sum Problem
# Given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation: