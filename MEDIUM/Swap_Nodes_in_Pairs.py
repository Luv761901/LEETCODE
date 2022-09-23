a = []
if head == None:
    return None
while(head.next != None):
    a.append(head.val)
    head = head.next
a.append(head.val)
for i in range(len(a)-1):
    if i % 2 == 0 or i == 0:
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
head = ListNode()
node = head
for i in a:
    node.next = ListNode(i)
    node = node.next
head = head.next
return head
