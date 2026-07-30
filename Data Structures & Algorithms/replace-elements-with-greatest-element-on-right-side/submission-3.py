class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        right_max = -1

        if not arr:
            return []

        for j in range(arr_len-1,-1,-1):
            if arr[j] > right_max:
                temp = arr[j]
                arr[j] = right_max
                right_max = temp
            else:
                arr[j] = right_max
            
        return arr