class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr_len  = len(nums)
        freq = [[] for i in range(arr_len + 1)]
        count_dict = {}

        for i in range(arr_len):
            count_dict[nums[i]] = count_dict.get(nums[i],0) + 1

        
        for value,count in count_dict.items():
            freq[count].append(value)

        return_list = []

        for j in range(len(freq)-1,0,-1):
            for num in freq[j]:
                return_list.append(num)
                if len(return_list)==k:
                    return return_list
