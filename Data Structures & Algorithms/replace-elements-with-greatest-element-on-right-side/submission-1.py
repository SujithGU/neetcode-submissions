class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        arr_len = len(arr)
        max_element = -1
        for i in range(0,arr_len):
            if i!= (arr_len-1):
                max_element = arr[i+1]
            for j in range(i+1,arr_len):
                if arr[j] > max_element:
                    max_element = arr[j]

            new_arr.append(max_element)

        new_arr[-1] = -1

        return new_arr
