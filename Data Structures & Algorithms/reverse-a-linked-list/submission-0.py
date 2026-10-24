# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a pointer to prev and current, in this case it would be none and head
        prev, curr = None, head

        # while we have a current value
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev