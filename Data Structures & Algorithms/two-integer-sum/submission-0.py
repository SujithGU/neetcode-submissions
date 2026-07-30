class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_tracker = {}

        for i in range(len(nums)):
            to_find = target-nums[i]

            if sum_tracker.get(to_find) is not None:
                diff_idx = sum_tracker.get(to_find)
                if i < diff_idx:
                    return [i, diff_idx]
                else:
                    return [diff_idx,i]
            else:
                sum_tracker[nums[i]] = i
        
        