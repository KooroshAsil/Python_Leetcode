# 1726. Tuple with Same Product
class Solution:
    def TuplesOfSameProduct(self, nums: list[int]) -> int:
        counter = {nums[i]*nums[j] : 0 for i in range(len(nums)) for j in range(i)}
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                product = nums[i]*nums[j]
                ans += counter[product] * 8
                counter[product] += 1
        return ans
                
array = [1,2,4,5,10]
s = Solution()
s.TuplesOfSameProduct(array)                
