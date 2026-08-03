class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [nums[0]]

        for i in range(1,len(nums)):
            sum_val = nums[i] + self.prefix_sum[i-1]
            self.prefix_sum.append(sum_val)

    def sumRange(self, left: int, right: int) -> int:
        sum_right = self.prefix_sum[right]
        sum_left = self.prefix_sum[left-1] if left > 0 else 0
        return sum_right - sum_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)