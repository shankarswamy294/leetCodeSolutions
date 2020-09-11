# Find the sum of all left leaves in a given binary tree.
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

class Solution:
    def __init__(self):
        self.sum = 0

    def traverse(self, root):
        if not root:
            return
        if root.left and root.left.left == None and root.left.right == None:
            self.sum += root.left.val
        self.traverse(root.left)
        self.traverse(root.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.traverse(root);
        return self.sum
