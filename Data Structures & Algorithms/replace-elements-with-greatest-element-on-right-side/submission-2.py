class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        right_max = -1
        ans = [0]*arr_len
        for i in range(arr_len-1,-1,-1):
            ans[i] = right_max
            right_max = max(arr[i],right_max)

        return ans
