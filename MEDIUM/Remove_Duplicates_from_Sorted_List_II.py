class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        a, b = [], []
        curr = head
        while(curr):
            a.append(curr.val)
            curr = curr.next
        for i in a:
            if a.count(i) == 1:
                b.append(i)
        print(b)
        h = ListNode()
        node = h
        for i in b:
            node.next = ListNode(i)
            node = node.next
        h = h.next
        return h
