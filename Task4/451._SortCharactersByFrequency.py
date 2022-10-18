class Solution:
    def frequencySort(self, s: str) -> str:
        countSmb = dict()
        for smb in s:
            countSmb[smb] = countSmb.get(smb, 0) + 1
        return ''.join(smb * countSmb[smb] for smb in \
            sorted(countSmb, key=countSmb.get, reverse=True))


a = Solution()
print(a.frequencySort("Aabb"))
