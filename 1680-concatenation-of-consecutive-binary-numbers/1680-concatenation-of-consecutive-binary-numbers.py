class Solution:
    def concatenatedBinary(self, n: int) -> int:
        new = ""
        for i in range(1,n+1):
            new += (bin(i)[2:])
        return int(new,2)%((10**9)+7)
