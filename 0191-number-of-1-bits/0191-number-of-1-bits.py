class Solution:
    def hammingWeight(self, n: int) -> int:
        t = int(bin(n)[2:])
        res = 0
        while t:
            res = res + t % 10
            t = t // 10
        
        return res
