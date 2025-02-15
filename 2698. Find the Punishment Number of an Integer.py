class Solution:
    def get_partitions(self,s, target):
        def backtrack(start, path):
            if start == len(s):
                if sum(path) == target:
                    partitions.append(path)
                return
            
            for end in range(start + 1, len(s) + 1):
                num = int(s[start:end])
                backtrack(end, path + [num])
        
        partitions = []
        backtrack(0, [])
        return partitions

    def punishmentNumber(self, n: int) -> int:
        punishment_number = 0

        for k in range(1,n+1):
            string = str(k**2)
            if len(self.get_partitions(string, int(k))) > 0:
                punishment_number += k**2

        return punishment_number

s = Solution()
print(s.punishmentNumber(10))