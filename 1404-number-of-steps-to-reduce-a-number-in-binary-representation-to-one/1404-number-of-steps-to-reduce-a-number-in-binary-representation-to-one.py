class Solution:
    def numSteps(self, s: str) -> int:
        new = int(s,2)
        cnt = 0
        while new != 1:
            if new % 2 == 0:
                new >>= 1
                cnt += 1

            else:
                new += 1
                cnt += 1
        return cnt