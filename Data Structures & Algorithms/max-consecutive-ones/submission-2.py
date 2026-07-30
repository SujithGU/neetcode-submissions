class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_max=0
        for num in nums:
            if num == 1:
                max_ones+=1
            else:
                if current_max < max_ones:
                    current_max = max_ones
                max_ones=0
        if current_max > max_ones:
            return current_max
        else:
            return max_ones