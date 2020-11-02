# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.decimalPlace = 0
        self.sum = 0

    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return

        self.getDecimalValue(head.next)
        if self.decimalPlace == 0 and head.val:
            self.sum += 1
        elif head.val:
            self.sum += 2 ** self.decimalPlace
        self.decimalPlace += 1

        return self.sum
