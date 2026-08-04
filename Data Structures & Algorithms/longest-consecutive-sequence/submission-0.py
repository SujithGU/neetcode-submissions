class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dd = defaultdict(int)

        res = 0

        for num in nums:
            if not dd[num]:
                dd[num] = dd[num-1] + dd[num+1] + 1
                dd[num - dd[num-1]] = dd[num]
                dd[num + dd[num+1]] = dd[num]

                res = max(res,dd[num])

        return res