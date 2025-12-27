from math import sqrt
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)
        d = 0
        t = 0
        for i in range(n):
            di = sqrt(dimensions[i][0]*dimensions[i][0] + dimensions[i][1]*dimensions[i][1])
            area = (dimensions[i][0] * dimensions[i][1])
            if d < di or (area > max_area and di == d):
                d = di
                max_area = area
        return max_area
        