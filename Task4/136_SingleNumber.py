from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numFreq = dict()
        for n in nums:
            if not numFreq.get(n, 0):
                numFreq[n] = 1
            else:
                numFreq.pop(n)
        return list(numFreq.keys())[0]

a = Solution()
print(a.singleNumber([2,2,1]))