# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dubhash = {}
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
                if hash[i] == 2:
                    dubhash[i] = True
                elif hash[i] == 3:
                    dubhash.pop(i, None)
            else:
                hash[i] = 1

        return list(dubhash.keys())