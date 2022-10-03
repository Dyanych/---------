from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range (len(nums)):
            sum += nums[i] - i - 1
        return -1 * sum

a = Solution()
print(a.missingNumber([3, 0, 1]))
