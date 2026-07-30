class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix:
            m = len(matrix)
            n = len(matrix[0])

            for i in range(m):
                mat = matrix[i]
                low = 0
                high = n-1

                if target >= mat[low] and target <= mat[high]:
                    while low <= high:
                        mid = (low+high)//2
                        if target == mat[mid]:
                            return True
                        elif mat[mid]< target:
                            low = mid+1
                        else:
                            high = mid-1
                else:
                    continue
            return False
        else:
            return False