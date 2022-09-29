class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if not head.val:
                return True
            head.val = None
            head = head.next
        return False
