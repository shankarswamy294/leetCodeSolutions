# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.


# Example:
#
# Input: 3
# Output: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        grid = [[0 for x in range(rowIndex + 1)] for y in range(rowIndex + 1)]
        if rowIndex == 0:
            return [1]
        else:
            grid[0][0] = 1

        for i in range(1, rowIndex + 1):
            for j in range(i + 1):
                if j - 1 >= 0:
                    grid[i][j] = grid[i - 1][j] + grid[i - 1][j - 1]
                else:
                    grid[i][j] = grid[i - 1][j]
        return grid[-1]
