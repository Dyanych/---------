from typing import List, Optional

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         return sorted(set(i for i in range(1, len(nums) + 2)) - set(nums))[0]

def qSort(arr: list) -> list:
    if arr:
        pivot = [x for x in arr if x == arr[0]]
        lesser = [x for x in arr[1:] if x < arr[0]]
        greater = [x for x in arr[1:] if x > arr[0]]
        return qSort(lesser) + pivot + qSort(greater)
    else:
        return []

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         numsSet = set(nums)
#         i = 0
#         for i in range(1, len(nums) + 1):
#             if i not in numsSet:
#                 return i
#         return i + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            # print(i, ' -> ', nums, nums[i], ' <--> ', nums[nums[i]-1])
            if nums[i] > 0 and nums[i] <=n and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
                

a = Solution()

print(a.firstMissingPositive([3,4,-1,1]))