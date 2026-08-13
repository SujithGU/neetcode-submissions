# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []

        result_list = [pairs.copy()]

        for i in range(1,len(pairs)):
            j = i-1
            state_result = pairs.copy()
            while j >= 0 and state_result[j].key > state_result[j+1].key:
                # swap
                temp = state_result[j]
                state_result[j] = state_result[j+1]
                state_result[j+1] = temp

                j-=1

                # result_list.append(state_result)
                pairs = state_result

            result_list.append(pairs)

        return result_list