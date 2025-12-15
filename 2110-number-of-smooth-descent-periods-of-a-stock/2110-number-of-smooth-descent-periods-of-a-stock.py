class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        cnt = 1
        total = 0
        ans = 0
        for i in range(1, n):
            if prices[i] == (prices[i-1] - 1):
                cnt += 1
            else:
                total = (cnt * (cnt+1)) // 2
                ans += total
                cnt = 1
        ans += cnt * (cnt + 1)//2
        return ans