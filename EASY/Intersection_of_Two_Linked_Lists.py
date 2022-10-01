class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            if l1 == None:
                l1 = headB
            elif l1 != None:
                l1 = l1.next
            if l2 == None:
                l2 = headA
            elif l2 != None:
                l2 = l2.next
        return l1
