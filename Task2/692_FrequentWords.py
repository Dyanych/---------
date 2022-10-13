from typing import List
from collections import Counter

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         frequency = dict()
#         for word in words:
#             frequency.update({word:(frequency.get(word,0) + 1)})
#         return frequency

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # frequency = Counter(words).items()
        return [_[0] for _ in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))][:k]

a = Solution()
print(a.topKFrequent(["i","love","leetcode","i","love","coding"], 2))