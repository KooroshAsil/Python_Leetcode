class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        mh = MinHeap()
        for element in nums:
            mh.insert(element)
        g = 0
        while True:
            if len(mh.heap) <  2:
                break
            elif mh.get_min() >= k:
                return g
            else:
                a = mh.extract_min()
                b = mh.extract_min()
                c = 2*a + b
                mh.insert(c)
                g += 1
        return g

s = Solution()
o = s.minOperations(nums = [2,11,10,1,3], k = 10)
print(o)