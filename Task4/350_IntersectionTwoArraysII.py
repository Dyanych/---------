from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = dict()
        res = list()
        if len(nums1) > len(nums2):
            for n in nums1:
                count[n] = count.get(n, 0) + 1
            for n in nums2:
                if count.get(n, 0) > 0:
                    res.append(n)
                    count[n] -= 1
        else:
            for n in nums2:
                count[n] = count.get(n, 0) + 1
            for n in nums1:
                if count.get(n, 0) > 0:
                    res.append(n)
                    count[n] -= 1
        return res
        
        




a = Solution()
print(a.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))