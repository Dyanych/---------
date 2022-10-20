from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([smb * n for smb, n in Counter(s).most_common()])

a = Solution()
print(a.frequencySort("Aabb"))
