class Solution:
    def isPalindrome(self, s, i, j):
        if i == j or i > j:
            return True
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def getPartition(self, s, i, j):
        if i >= j:
            return 0
        if self.t[i][j] != -1:
            return self.t[i][j]
        if self.isPalindrome(s, i, j):
            return 0
        min_ = len(s)+1
        for k in range(i, j):
            # temp=1+self.getPartition(s,i,k)+self.getPartition(s,k+1,j)
            if self.t[i][k] != -1:
                left = self.t[i][k]
                self.t[i][k] = left
            else:
                left = self.getPartition(s, i, k)

            if self.t[k + 1][j] != -1:
                right = self.t[k + 1][j]
                self.t[k + 1][j] = right
            else:
                right = self.getPartition(s, k + 1, j)
            temp = 1 + left + right
            min_ = min(min_, temp)

        self.t[i][j] = min_
        return self.t[i][j]

    def minCut(self, s: str) -> int:
        self.t = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
        return self.getPartition(s, 0, len(s) - 1)


if __name__ == '__main__':
    s = Solution()
    inp ="adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
    ans = s.minCut(inp)
    print(ans)