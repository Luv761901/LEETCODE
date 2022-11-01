# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []:
            return None
        c, c1 = 0, 0
        curr = head
        while(curr.next != None):
            c += 1
            curr = curr.next
        c += 1
        if c == 1:
            return None
        s = c//2
        curr1 = head
        while(curr1.next != None):
            c1 += 1
            curr1 = curr1.next
            if c1 == s:
                break
        print(curr1.val)
        curr2 = head
        while(head.next != curr1):
            head = head.next
        head.next = curr1.next
        curr1 = None
        return curr2
