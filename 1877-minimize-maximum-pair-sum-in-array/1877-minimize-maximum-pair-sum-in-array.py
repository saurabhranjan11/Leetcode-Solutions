class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = []
        i, j = 0, n-1
        while i < j:
            res.append(nums[i] + nums[j])
            i += 1
            j -= 1
        return max(res)
        