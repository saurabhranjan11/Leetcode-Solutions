class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=1:
            return n
        small =  min(nums)
        large = max(nums)
        new = []
        for i in range(n):
            if nums[i] == small:
                new.append(i)
            if nums[i] == large:
                new.append(i)
        
        i = min(new)
        j = max(new)
        front = j + 1
        back = n-i
        total = (i+1) +(n-j)
        return min(front, back, total)