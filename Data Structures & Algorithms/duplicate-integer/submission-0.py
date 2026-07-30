class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr_len = len(nums)

        tracker_dict = {}

        for i in range(arr_len):
            if tracker_dict.get(nums[i]) is not None:
                
                return True
            else:
                tracker_dict[nums[i]] = i
        
        return False 