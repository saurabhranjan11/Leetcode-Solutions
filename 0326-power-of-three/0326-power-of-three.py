class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        for i in range(n):
            total = 3**i
            if total > n:
                return False
            if 3**i == n:
                return True
        return False
            