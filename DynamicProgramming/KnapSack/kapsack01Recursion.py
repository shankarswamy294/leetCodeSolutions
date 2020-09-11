# code
class Solution():
    def __init__(self):
        pass

    def knapsack(self, wt, val, N, W):
        if not N or not W:
            return 0

        if wt[N - 1] <= W:
            return max(val[N - 1] + self.knapsack(wt, val, N - 1, W - wt[N - 1]), self.knapsack(wt, val, N - 1, W))
        else:
            return self.knapsack(wt, val, N - 1, W)


test_cases = input()
for i in range(int(test_cases)):
    N = int(input())
    W = int(input())
    val = [int(i) for i in input().split(" ")]
    wt = [int(i) for i in input().split(" ")]
    s = Solution()
    print(s.knapsack(wt, val, N, W))
