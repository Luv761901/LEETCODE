class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        arr = []
        while(head.next != None):
            arr.append(head.val)
            head = head.next
        arr.append(head.val)
        print(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while(j >= 0 and key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        head1 = ListNode()
        node = head1
        for i in arr:
            node.next = ListNode(i)
            node = node.next
        head1 = head1.next
        return head1
