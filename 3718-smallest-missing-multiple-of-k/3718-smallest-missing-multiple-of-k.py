class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        new = set(nums)
        multiple = k
        while multiple in new:
            multiple += k
        return multiple