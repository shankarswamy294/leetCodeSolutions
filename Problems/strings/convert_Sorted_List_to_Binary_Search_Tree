# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMiddleElement(self, head):
        if not head.next: return head,None
        temp,temp1=head,head.next
        prev=None
        
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        return temp,prev
    
    def buildTree(self, list_head):
        if not list_head:
            return None
        middleElem, prev = self.getMiddleElement(list_head)
        root=TreeNode(middleElem.val)
        if prev: 
            prev.next=None
            root.left=self.buildTree(list_head)
        root.right=self.buildTree(middleElem.next)
        return root
            
        
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.buildTree(head)
        
        
        
