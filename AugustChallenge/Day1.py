# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

# Example1:
#
# Input: "USA"
# Output: True
#
# Example2:
#
# Input: "FlaG"
# Output: False

class Solution(object):
    def detectCapitalUse(self, word):
        cap = 0
        sC = False
        for ind, i in enumerate(word):
            if ind == 0 and ord(i) >= 65 and ord(i) <= 90:
                sC = True
            if ord(i) >= 65 and ord(i) <= 90:
                cap += 1

        if cap == 1 and sC:
            return True

        if cap == len(word):
            return True

        if cap == 0:
            return True

        return False