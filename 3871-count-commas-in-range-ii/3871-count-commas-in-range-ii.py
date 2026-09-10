class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 0
        start = 1000
        while start<=n:
            cnt += (n - start + 1)
            start *= 1000
        return cnt