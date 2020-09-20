class Solution():
    def __init__(self, n, m):
        self.dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    def lcs(self, str1, str2, n, m):
        if not n or not m:
            return 0
        if self.dp[n][m] != -1:
            return self.dp[n][m]
        else:
            if str1[n-1]==str2[m-1]:
                self.dp[n][m] = 1 + self.lcs(str1, str2, n-1, m-1)
            else:
                self.dp[n][m] = max(self.lcs(str1, str2, n-1, m), self.lcs(str1, str2, n, m-1))

        return self.dp[n][m]

# str1="abc"
# str2="def"
str1="abcde"
str2="ace"
s = Solution(len(str1), len(str2))
print(s.lcs(str1, str2, len(str1), len(str2)))