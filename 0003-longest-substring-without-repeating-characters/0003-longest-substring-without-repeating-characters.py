class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        new = set()
        i = 0
        for j in range(len(s)):
            while s[j] in new:
                new.remove(s[i])
                i += 1
            new.add(s[j])
            res = max(res,j-i+1)
        return res