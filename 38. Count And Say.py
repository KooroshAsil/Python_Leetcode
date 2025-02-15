class Solution:
    def countAndSay(self, n: int) -> str:
        if not n in range(1,31) : 
            return "Invalid Integer"
        elif n == 1 : 
            return "1"
        else :
            return self.runlengthcode(self.countAndSay(n-1))
                        
    def runlengthcode(self,s:str) -> str:
        l = [k for k in s]
        count = []
        number = []
        i = 0
        while i <len(l):
            m = l[i]
            j = i+1 
            c = 1
            if j > len(l) :
                break
            while True:
                if j >= len(l) :
                    break 
                flag = (m == l[j])
                if flag:
                    c += 1
                    j += 1
                else:
                    break
            count.append(str(c))
            number.append(str(m))
            i += c

        concatenated = [''.join(pair) for pair in zip(count, number)]
        code = result_string = ''.join(concatenated)
        return code

s = Solution()
n= int(input())
s.countAndSay(n)
print(s.countAndSay(n))        
        
