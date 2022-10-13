from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diffCandies = (sum(aliceSizes) - sum(bobSizes)) // 2
        for aliceBox in set(aliceSizes):
            if (aliceBox - diffCandies) in set(bobSizes):
                    return [aliceBox, aliceBox - diffCandies]
        return None

a = Solution()
print(a.fairCandySwap([1,17,14,1,16], [26,11]))