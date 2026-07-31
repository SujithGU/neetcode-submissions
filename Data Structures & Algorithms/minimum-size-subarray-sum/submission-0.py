class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_window = len(nums)+1
        
        win_total = 0

        for R in range(len(nums)):
            win_total += nums[R]

            while win_total>=target:
                min_window = min(min_window,R-L+1)
                win_total -= nums[L]
                L+=1

        return 0 if min_window==len(nums)+1 else min_window