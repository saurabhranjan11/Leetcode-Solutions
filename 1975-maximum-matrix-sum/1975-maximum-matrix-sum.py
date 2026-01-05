class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cnt = 0
        new = float('inf')
        total = 0
        zero = False
        for row in matrix:
            for x in row:
                total += abs(x)
                new = min(new,abs(x))
                if x == 0:
                    zero = True
                if x < 0:
                    cnt += 1
        if cnt % 2 != 0 and not zero:
            total -= (2*new)

        return total