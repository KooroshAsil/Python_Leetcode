import numpy as np

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        """moving like spiral in an n*n matrix and 
            filling its values"""
        array = np.zeros((n,n))
        i = 0
        j = 0 
        k = 1

        while np.any(array == 0):
            while True:
                if j >= n :
                    j -= 1
                    i+=1
                    break
                if array[i][j] != 0:
                    i+= 1
                    j-= 1
                    break
                array[i][j] = k
                k+= 1
                j += 1
            while True:
                if i >= n :
                    i -= 1
                    j -= 1
                    break
                if array[i][j] != 0:
                    j-= 1
                    i-= 1
                    break
                array[i][j] = k
                k+= 1
                i += 1

            while True:
                if j < 0 :
                    j += 1
                    i-= 1
                    break
                if array[i][j] != 0:
                    j += 1
                    i-= 1
                    break
                array[i][j] = k
                k+=1 
                j -= 1
            while True:
                if i<0 :
                    i+= 1
                    j+=1
                    break
                if array[i][j] != 0:
                    i+= 1
                    j+=1
                    break
                array[i][j] = k
                k+= 1
                i -= 1
        array = array.astype(int)
        nested_list = array.tolist()
        return nested_list

s = Solution()
print(s.generateMatrix(n = 5))