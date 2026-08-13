# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_helper(pairs,0,len(pairs)-1)

    def merge_helper(self,arr,start,end):
        
        if (end-start + 1 <= 1):
            return arr

        mid = (end + start) // 2

        self.merge_helper(arr,start,mid)
        self.merge_helper(arr,mid+1,end)

        self.merge(arr,start,mid,end)

        return arr

    def merge(self,arr,start,mid,end):
        arr_1 = arr[start:mid+1]
        arr_2 = arr[mid+1:end+1]

        i,j,k = 0, 0, start

        while i< len(arr_1) and j< len(arr_2):
            if arr_1[i].key <= arr_2[j].key:
                arr[k] = arr_1[i]
                i+=1
            else:
                arr[k] = arr_2[j]
                j+=1
            k+=1
            
        while i < len(arr_1):
            arr[k] = arr_1[i]
            i+=1
            k+=1

        while j < len(arr_2):
            arr[k] = arr_2[j]
            j+=1
            k+=1

