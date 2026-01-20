class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []  
        found = False
        for i in range(n):
            for j in range(nums[i]):
                if (j | (j+1)) == nums[i]:
                    res.append(j)
                    found = True
                    break
            if not found:
                res.append(-1)
            else:
                found = False
        return res