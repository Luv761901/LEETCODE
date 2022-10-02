class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        p = None
        p1 = head
        while p1:
            if p1.val == val:
                p.next = p1.next
            else:
                p = p1
            p1 = p1.next
        return head
