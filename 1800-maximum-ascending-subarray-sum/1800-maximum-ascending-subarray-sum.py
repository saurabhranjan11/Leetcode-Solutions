class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        tot = nums[0]
        n = len(nums)
        res = nums[0]
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                tot += nums[i]
            else:
                tot = nums[i]
            res = max(res,tot)
        return res