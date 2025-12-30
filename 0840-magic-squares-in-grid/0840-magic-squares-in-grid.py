class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0

        def isMagic(i, j):
            nums = set()

            # check numbers 1–9 and uniqueness
            for r in range(3):
                for c in range(3):
                    val = grid[i+r][j+c]
                    if val < 1 or val > 9 or val in nums:
                        return False
                    nums.add(val)

            # check rows and columns
            for k in range(3):
                if sum(grid[i+k][j:j+3]) != 15:
                    return False
                if grid[i][j+k] + grid[i+1][j+k] + grid[i+2][j+k] != 15:
                    return False

            # check diagonals
            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15:
                return False
            if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15:
                return False

            return True

        count = 0
        for i in range(n - 2):
            for j in range(m - 2):
                # optimization: center must be 5
                if grid[i+1][j+1] == 5 and isMagic(i, j):
                    count += 1

        return count
