a = []
for i in lists:
    while i != None:
        a.append(i.val)
        i = i.next
a.sort()
if len(a) == 0:
    return None
head = ListNode()
node = head
for i in a:
    node.next = ListNode(i)
    node = node.next
head = head.next
return head
