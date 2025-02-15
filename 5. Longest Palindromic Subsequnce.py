class Solution:
    def __init__(self):
        self.s = None
        self.opt = None
        self.ispal = None

    def check_equality(self, i, j):
        return self.s[i] == self.s[j]

    def setter(self, s):
        self.s = s
        n = len(s)
        self.opt = [[-1 for _ in range(n)] for _ in range(n)]  
        self.ispal = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self.ispal[i][i] = True

    def longest_palindrome(self, i, j):
        if i > j:
            return 0

        if i == j:
            self.opt[i][j] = 1
            self.ispal[i][j] = True
            return 1

        if self.opt[i][j] != -1:  
            return self.opt[i][j]

        if self.check_equality(i, j):
            if i + 1 == j:
                self.opt[i][j] = 2
                self.ispal[i][j] = True
            else:
                inner_length = self.longest_palindrome(i + 1, j - 1)
                if self.ispal[i + 1][j - 1]:
                    self.opt[i][j] = 2 + inner_length
                    self.ispal[i][j] = True
                else:
                    self.opt[i][j] = max(self.longest_palindrome(i + 1, j), 
                                         self.longest_palindrome(i, j - 1))
        else:
            self.opt[i][j] = max(self.longest_palindrome(i + 1, j), 
                                 self.longest_palindrome(i, j - 1))

        return self.opt[i][j]
    
    def longestPalindrome(self,s):
        n = len(s) - 1
        self.setter(s)
        a = self.longest_palindrome(0, n)
        return self.palindrome(a)
                
    def palindrome(self, a):
        ans = []
        n = len(self.s)

        for i in range(n):
            for j in range(i, n):
                if self.opt[i][j] == a and self.ispal[i][j]:
                    ans.append((i, j + 1))  

        strings = [self.s[start:end] for start, end in ans]
        return strings

s = "charachter"
solver = Solution()
print(solver.longestPalindrome(s))
