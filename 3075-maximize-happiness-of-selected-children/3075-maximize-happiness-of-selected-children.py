class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort(reverse = True)
        for i in range(k):
            happiness[i] -= i
            if happiness[i] <= 0:
                break
            res += happiness[i]
            
        return res
