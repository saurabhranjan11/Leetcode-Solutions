class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = {}
        cnt = 0
        for num in nums:
            mp[num] = mp.get(num,0) + 1

        max_freq = max(mp.values())
        cnt = 0
        for val in mp.values():
            if val == max_freq:
                cnt += val
        return cnt