class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            prefix[i] = curr_max

        suffix = [0] * n
        curr_min = float('inf')
        for i in range(n-1,-1,-1):
            curr_min = min(curr_min, nums[i])
            suffix[i] = curr_min
        for i in range(n):
            if (prefix[i] - suffix[i]) <= k:
                return i
        return -1