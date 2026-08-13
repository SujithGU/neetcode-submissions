class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr_1 = nums1[:m]
        arr_2 = nums2[:n]

        i, j, k = 0, 0, 0

        while i< len(arr_1) and j < len(arr_2):
            if arr_1[i] <= arr_2[j]:
                nums1[k] = arr_1[i]
                i+=1
                k+=1
            else:
                nums1[k] = arr_2[j]
                j+=1
                k+=1
        
        while i< len(arr_1):
            nums1[k] = arr_1[i]
            i+=1
            k+=1
        while j < len(arr_2):
            nums1[k] = arr_2[j]
            j+=1
            k+=1