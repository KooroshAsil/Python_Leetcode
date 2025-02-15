class Solution:
    def match(self,text1,text2,i,j) :
        if text1[i] == text2[j]:
            return 1 
        else:
            return 0 

    def longestCommonSubsequence_recursivememoization(self, text1: str, text2: str,
            memo = None, i = None, j = None) -> int:

        if memo is None:
            n,m = len(text1),len(text2)
            memo = [[-1 for i in range(m)] for j in range(n)]
            i,j = n-1,m-1

        if i+1 == 0 or j+1 == 0:
            return 0
        elif memo[i][j] != -1:
            return memo[i][j]
        else:
            memo[i][j] = max(
                self.longestCommonSubsequence(text1,text2, memo, i-1, j-1) + self.match(text1, text2, i,j),
                self.longestCommonSubsequence(text1,text2, memo, i, j-1),
                self.longestCommonSubsequence(text1,text2, memo, i-1, j)    
            ) 
            return memo[i][j]

    def longestCommonSubsequence_dp(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n][m]

text1 = "abc"
text2 = "def"
s = Solution()
print((s.longestCommonSubsequence_dp(text1, text2)))
