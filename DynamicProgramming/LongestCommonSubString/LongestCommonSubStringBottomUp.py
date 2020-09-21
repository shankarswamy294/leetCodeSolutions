class Solution():
    def __init__(self, n, m):
        self.dp = [[0 for i in range(m+1)] for j in range(n+1)]
        self.max=0

    def lcs(self, str1, str2, n, m):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    self.dp[i][j] = 1 + self.dp[i-1][j-1]
                    self.max = max(self.max, self.dp[i][j])
                else:
                    self.dp[i][j] = 0

        return self.max

# str1="abc"
# str2="def"
str1="abcde"
str2="abce"
s = Solution(len(str1), len(str2))
print(s.lcs(str1, str2, len(str1), len(str2)))