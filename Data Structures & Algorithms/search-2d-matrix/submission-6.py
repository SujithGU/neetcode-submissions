class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix:
            row_len = len(matrix)
            col_len = len(matrix[0])

            top = 0
            bottom = row_len - 1

            while top <= bottom:
                row = (top+bottom)//2
                if target > matrix[row][-1]:
                    top = row+1
                elif target < matrix[row][0]:
                    bottom = row-1
                else:
                    break
                
            # row = (top + bottom) // 2
            low = 0
            high = col_len-1

            while low <= high:
                mid = (low+high)//2
                if target == matrix[row][mid]:
                    return True
                elif matrix[row][mid]< target:
                    low = mid+1
                else:
                    high = mid-1

            return False