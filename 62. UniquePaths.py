def recursive_UniquePaths(m, n):
    if m < 0 or n < 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    elif m == 1: 
        return 1
    elif n == 1: 
        return 1
    else:
        return recursive_UniquePaths(m - 1, n) + recursive_UniquePaths(m, n - 1)

def dp_UniquePaths(m,n):
    dp = [[0 for j in range(n) ] for i in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp [i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1], dp 
    
m,n = 3,7
result , table = dp_UniquePaths(m,n)
print("The number of unique paths:",result)
print("dp table = cost of going from (0,0) to (i,j):")
for k in table:
    print(k)
