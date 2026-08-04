class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r_len , col_len = len(matrix),len(matrix[0])

        self.sum_mat = [[0]*(col_len+1) for row in range(r_len+1)]

        for row in range(r_len):
            prefix_sum  = 0
            for col in range(col_len):
                prefix_sum += matrix[row][col]
                above = self.sum_mat[row][col+1]

                self.sum_mat[row+1][col+1] = prefix_sum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottom_right = self.sum_mat[row2][col2]
        above = self.sum_mat[row1-1][col2]
        left = self.sum_mat[row2][col1-1]
        top_left = self.sum_mat[row1-1][col1-1]

        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)