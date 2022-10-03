from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum, i = 0, 1
        for x in nums:
            sum += i - x
            i +=1
        return sum

a = Solution()
print(a.missingNumber([3, 0, 1]))
