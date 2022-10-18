class Solution:
    def frequencySort(self, s: str) -> str:
        countSmb = dict()
        for smb in s:
            countSmb[smb] = countSmb.get(smb, 0) + 1
        return ''.join([smb[0] * smb[1] for smb in \
        sorted(countSmb.items(), key=lambda _: _[1], reverse=True)])


a = Solution()
print(a.frequencySort("Aabb"))
