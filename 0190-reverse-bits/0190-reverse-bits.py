class Solution:
    def reverseBits(self, n: int) -> int:
        nums = bin(n)[2:]
        nums = nums.zfill(32)
        rev = nums[::-1]
        return int(rev,2)