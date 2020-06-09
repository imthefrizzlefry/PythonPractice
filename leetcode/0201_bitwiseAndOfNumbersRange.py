class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k = 0
        while n != m:
            n >>= 1
            m >>= 1
            k += 1
        return n << k


temp = Solution()

print(temp.rangeBitwiseAnd(200000, 2147483647))

print(temp.rangeBitwiseAnd(3,5))

print(temp.rangeBitwiseAnd(0,1))

print(temp.rangeBitwiseAnd(5,7))

print(temp.rangeBitwiseAnd(65,127))