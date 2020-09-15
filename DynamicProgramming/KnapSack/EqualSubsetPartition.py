# User function Template for Python3

class Solution:

    def subsetSum(self, N, arr, sum):
        t =  [[0 for i in range(sum)] for j in range(N + 1)]
        for i in range(N + 1):
            for j in range(sum + 1):
                if i == 0:
                    t[i][j] = 0
                elif j == 0:
                    t[i][j] = 1
                else:
                    if arr[i - 1] <= j:
                        t[i][j] = t[i - 1][j - (arr[i - 1])] or t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]
                return t[N][sum]

    def equalPartition(self, N, arr):
        totalSum = 0
        for i in arr:
            totalSum += i

        if not totalSum % 2:
            return self.subsetSum(N, arr, totalSum/2)
        else:
            return False


# {
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends