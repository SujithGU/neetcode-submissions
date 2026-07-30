class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_arr = []

        for idx,value in enumerate(operations):
            if value != '+' and value != 'D' and value != 'C':
                sum_arr.append(int(value))
            elif value == '+':
                sum_arr.append(sum_arr[-2] + sum_arr[-1])
            elif value == 'D':
                sum_arr.append(2 * sum_arr[-1])
            else:
                sum_arr.pop()
        
        total_sum = 0
        while len(sum_arr)>0:
            total_sum+=sum_arr.pop()

        return total_sum
