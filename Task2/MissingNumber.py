from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((2 * len(nums) + 1)**2 - 1)//8 - sum(nums) 

a = Solution()
print(a.missingNumber([3, 0, 1]))
