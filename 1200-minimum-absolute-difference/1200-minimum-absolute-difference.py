class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        res = []
        diff = 0
        mind = float("inf")
        for i in range(1,n):
            diff = abs(arr[i-1] - arr[i])
            mind = min(mind,diff)
        
        for i in range(1,n):
            new = abs(arr[i] - arr[i-1])
            if new == mind:
                res.append([arr[i-1],arr[i]])
        return res