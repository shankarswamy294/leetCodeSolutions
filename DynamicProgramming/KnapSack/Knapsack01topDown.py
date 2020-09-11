class Solution():
    def __init__(self, N, W):
        self.t=[[0 for i in range(W+1)] for j in range(N+1)]

    def knapsack(self, wt, val, N, W):
        if N<=0 or W<=0:
            return 0

        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1]<=j:
                    self.t[i][j] = max(val[i-1]+self.t[i-1][j-wt[i-1]], self.t[i-1][j])
                else:
                    self.t[i][j] = self.t[i-1][j]

        return self.t[N][W]

test_cases = input()
for i in range(int(test_cases)):
    N = int(input())
    W = int(input())
    val = list(map(int, input().split(' ')[:N]))
    wt = list(map(int, input().split(' ')[:N]))
    s = Solution(N,W)
    s.knapsack(wt, val, N, W)
    print(s.t)
    print(s.t[N][W])