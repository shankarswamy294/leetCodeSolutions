# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0;

    def searchPath(self, root, ps, n):
        if not root:
            return;
        ps += root.val
        if ps == n:
            self.count += 1

        self.searchPath(root.left, ps, n)
        self.searchPath(root.right, ps, n)

    def pathSum(self, root, sum):
        if not root:
            return self.count
        q = [root]
        while (q):
            x = q.pop()
            self.searchPath(x, 0, sum)
            if x.left:
                q.append(x.left)

            if x.right:
                q.append(x.right)

        return self.count
