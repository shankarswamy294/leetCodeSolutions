class Solution():
    def __init__(self):
        self.lcs_str = ""

    def lcs(self, str1, str2, n, m):
        if not n or not m:
            return 0
        else:
            if str1[n-1] == str2[m-1]:

                print(str1[n-1], n, m)
                self.lcs_str += str1[n-1]
                self.lcs(str1, str2, n-1, m-1)
            else:
                self.lcs(str1, str2, n-1, m)
                self.lcs(str1, str2, n, m-1)




s = Solution()
str1="abcde"
str2="ace"
# str1="abc"
# str2="abc"
s.lcs(str1, str2, len(str1), len(str2))
print(s.lcs_str[::-1])