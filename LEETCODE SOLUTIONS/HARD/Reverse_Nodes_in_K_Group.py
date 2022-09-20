a = []
x = head
while(x.next != None):
    a.append(x.val)
    x = x.next
a.append(x.val)
for i in range(0, len(a), k):
    if len(a[i:i+k]) == k:
        a[i:i+k] = a[i:i+k][::-1]
head = ListNode()
node = head
for i in a:
    node.next = ListNode(i)
    node = node.next
head = head.next
return head
