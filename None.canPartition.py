
class Solution:
    def canPartition(self, items, value, visited=None, partition=None):
        if visited is None:    
            visited = set()
            partitions = []
            partition = []
        
        if sum(partition) == value:
            return True
        
        for i in range(len(items)):
            element = items[i]
            if element not in visited:
                if sum(partition) + element <= value:
                    visited.add(element)
                    partition.append(element)                    

                    if self.canPartition(items[i+1:], value, visited, partition):
                        return True
                    partition.pop()
                    visited.remove(element)
        return False
        
s = Solution()
items = [1,3,9]
print(s.canPartition(items, 11)) 
