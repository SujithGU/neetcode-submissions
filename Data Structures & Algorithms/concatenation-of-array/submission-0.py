class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        ans = [0]*(2* arr_len)
        for i in range(arr_len):
            ans[i] = nums[i]
            concate_index = i+ arr_len
            ans[concate_index] = nums[i]
        
        return ans