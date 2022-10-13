# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x > 0 and x % 10 == 0):
#             return False
#         else:
#             pal = list()
#             while x:
#                 pal.append(x % 10)
#                 x //= 10
#             return pal == pal[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return x == 0
        else:
            revX = 0
            while x > revX:
                revX = revX *10 + x % 10
                x //= 10
            return (x == revX or x == revX // 10)

a = Solution()
y = 1000000000000001
print(y, a.isPalindrome(y))
            