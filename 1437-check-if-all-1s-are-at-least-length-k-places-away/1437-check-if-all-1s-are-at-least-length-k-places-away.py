class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag = float("-inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                if i <= flag+k:
                    return False
                flag = i
        return True
