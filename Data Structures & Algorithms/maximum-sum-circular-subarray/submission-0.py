class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min , curr_max = nums[0],nums[0]
        max_sum, min_sum = nums[0],nums[0]
        total = nums[0]

        for n in nums[1:]:
            curr_max = max(n,curr_max+n)
            curr_min = min(n,curr_min+n)

            max_sum = max(curr_max,max_sum)
            min_sum = min(curr_min,min_sum)

            total+=n
        
        if max_sum<0:
            return max_sum # all negatives scenario
        else:
            return max(max_sum,total-min_sum)