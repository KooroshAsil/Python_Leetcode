class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        pairs = [[] for _ in range((82))]
        for num in nums:
            n = self.sum_digits(num)
            pairs[n-1].append(num)

            if len(pairs[n-1]) > 2 :
                m = min(pairs[n-1])
                pairs[n-1].remove(m)
        maxpair = -1
        for pair in pairs:
            if len(pair) == 2 :
                if sum(pair) > maxpair :
                    maxpair = sum(pair)

        return maxpair
    
    def sum_digits(self,number):
        s = 0
        while number > 0 :
            n = number % 10
            number = int(number/10)
            s += n
        return s
    
    