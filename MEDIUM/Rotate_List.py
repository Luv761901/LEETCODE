class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        if head == None:
            return None
        while(head.next != None):
            a.append(head.val)
            head = head.next
        a.append(head.val)
        print(a)

        b = [0]*len(a)
        for i in range(len(a)):
            b[(i+k) % len(a)] = a[i]
        print(b)
        head = ListNode()
        node = head
        for i in b:
            node.next = ListNode(i)
            node = node.next
        head = head.next
        return head
