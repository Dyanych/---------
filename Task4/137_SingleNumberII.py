from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numFreq = {}
        # for n in nums:
        #     if numFreq.setdefault(n, 0) == 2:
        #         numFreq.pop(n)
        #     else:
        #         numFreq[n] += 1
        # return list(numFreq)[0]

        # for n in set(nums):
        #     try:
        #         nums.remove(n)
        #         nums.remove(n)
        #         nums.remove(n)
        #     except:
        #         break
        # return n

        ones, twos = 0, 0
        for n in nums:
            ones = (ones ^ n) & (~twos)
            twos = (twos ^ n) & (~ones)
        return ones 



a = Solution()
print(a.singleNumber([2,2,3,2]))