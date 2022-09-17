def numOfSubsetWithGivenDiff(arr,diff,n):
    sumArr = sum(arr)

    newSum = (sumArr + diff ) // 2

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
diff = int(input())
print(numOfSubsetWithGivenDiff(arr,diff,n))

# Given an array Arr[] and a difference diff, find the number of subsets that array can be divided so that each the difference between the two subset is the given diff.
#
# Example1:
# Input:
# Arr[] : 1,1,2,3
# diff: 1
# Output: 3 .

# Idea :
#     sum(sub1) - sum(sub2) = diff ------ 1
#     sum(sub1) + sum(sub2) = sum(arr) ---- 2
