# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.

#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        l, odd = 0, False
        for i in hash.keys():
            if hash[i] % 2 == 0:
                l += hash[i]
            else:
                if odd:
                    l += hash[i] - 1
                else:
                    l += hash[i]
                    odd = True
        return l