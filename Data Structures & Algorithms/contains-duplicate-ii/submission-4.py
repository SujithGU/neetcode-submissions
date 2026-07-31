import math

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L, R = 0,1

        if k == 0:
            return False
        
        hashset = set()
        hashset.add(nums[L])

        while R < len(nums):
            if abs(L-R)<=k:
                if nums[R] in hashset:
                    return True
                else:
                    hashset.add(nums[R])
                    R = R+1
            else:
                hashset.remove(nums[L])
                L = L+1
                hashset.add(nums[L])
                

        return False