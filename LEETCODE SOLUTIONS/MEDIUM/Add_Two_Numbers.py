s, p = "", ""
while(l1.next != None):
    s += str(l1.val)
    l1 = l1.next
s += str(l1.val)
while(l2.next != None):
    p += str(l2.val)
    l2 = l2.next
p += str(l2.val)
q = int(s[::-1])+int(p[::-1])
q = str(q)
q = q[::-1]
head = ListNode()
node = head
for i in q:
    node.next = ListNode(int(i))
    node = node.next
head = head.next
return head
