class Solution:
    def reverseDegree(self, s: str) -> int:
        collect = 0
        for i,ch in enumerate(s, start = 1):
            number = 26 - (ord(ch) - ord('a'))
            collect += i * number
        return collect