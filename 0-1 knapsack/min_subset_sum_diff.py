def minSubsetSumDiff(arr,n,rangee):
    dp = [[-1 for i in range(rangee+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,rangee+1):
        dp[0][i] = False

    for i in range(1,n+1):
        for j in range(1,rangee+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]


    l = []
    for i in range(0,rangee//2+1):
        if dp[n][i]==True:
            l.append(i)

    min_diff = 100000
    for i in l:
        min_diff = min(min_diff,rangee-2*i)
    return min_diff

arr = list(map(int,input().split()))
n = len(arr)
rangee = sum(arr)
print(minSubsetSumDiff(arr,n,rangee))


# Sum of subset differences
# Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
# If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
#
# Example:
# Input:  arr[] = {1, 6, 11, 5}
# Output: 1
# Explanation:
# Subset1 = {1, 5, 6}, sum of Subset1 = 12
# Subset2 = {11}, sum of Subset2 = 11