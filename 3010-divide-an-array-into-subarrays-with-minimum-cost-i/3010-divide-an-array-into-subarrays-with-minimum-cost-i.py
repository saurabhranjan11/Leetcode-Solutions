class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = float("inf")
        min2 = float("inf")
        first = nums[0]
        for num in nums[1:]:
            if min1 > num:
                min2 = min1
                min1 = num
            elif min2 > num:
                min2 = num
        return first + min1 + min2
