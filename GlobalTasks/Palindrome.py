class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            pal = list()
            while x:
                pal.append(x%10)
                x //= 10
            for i in range(len(pal)//2):
                if pal[i] != pal[-i-1]:
                    return False
            return True
            