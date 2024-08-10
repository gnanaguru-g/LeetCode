# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, currentNode = head.next, head.next
        s=0
        while currentNode != None:

            if currentNode.val != 0:
                s+=currentNode.val
            else:
                prevNode.val = s
                prevNode.next = currentNode.next
                prevNode = currentNode.next
                s = 0            
            currentNode = currentNode.next
        return head.next