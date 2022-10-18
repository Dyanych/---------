from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        j = 1
        while nums:
            try:
                if nums[0] != nums[j]:
                    nums.pop(j)
                    nums.pop(0)
                    j = 1
                else:
                    j += 1
            except:
                break
        return nums[0]

    
a = Solution()
print(a.majorityElement([3,2,3]))