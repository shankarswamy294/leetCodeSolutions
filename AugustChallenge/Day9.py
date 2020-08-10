# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, tm, c1 = collections.deque([]), 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    c1 += 1
                elif grid[i][j] == 2:
                    q.append([i, j, 0])

        while q:
            i, j, m = q.popleft()
            if m > tm:
                tm = m
            if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                c1 -= 1
                q.append([i, j + 1, m + 1])
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                c1 -= 1
                q.append([i, j - 1, m + 1])
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                c1 -= 1
                q.append([i + 1, j, m + 1])
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                c1 -= 1
                q.append([i - 1, j, m + 1])
        if c1:
            return -1

        return tm