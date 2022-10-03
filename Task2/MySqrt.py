class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x in (1, 2, 3):
            return 1
        elif x in (4, 5):
            return 2
        
        start, end = 0, x //2
        print(start, end)
        while (end - start) > 1:
            middle =(start + end) // 2

            if (middle * middle) < x:
                start = middle
            elif (middle * middle) > x:
                end = middle
            else:
                return middle
            print(start, middle, end)
        else:
            return start

    def mySqrt1(self, x: int) -> int:
        i = 0
        while i*i <= x:
            i += 1
        return i-1

a = Solution()

print(a.mySqrt1(8))
