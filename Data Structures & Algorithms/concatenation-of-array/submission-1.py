class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)

        concat_arr = [0]* 2 * arr_len

        if not nums:
            return []
        else:
            for i in range(arr_len):
                concat_arr[i] = nums[i]
                concat_arr[i+(arr_len)] = nums[i]

        return concat_arr
