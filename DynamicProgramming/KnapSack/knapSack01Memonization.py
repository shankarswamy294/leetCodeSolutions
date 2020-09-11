class Solution():
    def __init__(self, N, W):
        self.t=[[-1] * (W+1)] * (N+1)

    def knapsack(self, wt, val, N, W):
        if N<=0 or W<=0:
            return 0
        if self.t[N][W] > -1:
            return self.t[N][W]
        if wt[N - 1] <= W:
            self.t[N][W] = max(val[N - 1] + self.knapsack(wt, val, N - 1, W - wt[N - 1]), self.knapsack(wt, val, N - 1, W))
        else:
            self.t[N][W] = self.knapsack(wt, val, N - 1, W)
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