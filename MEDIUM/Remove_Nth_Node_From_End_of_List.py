n -= 1
temp = head
ptr = head
ptr2 = head
ptr3 = head
c = 0
while(temp.next != None):
    temp = temp.next
    c += 1
s = c-n
if s == 0:
    head = head.next
    return head

if c == 0:
    head = None
    return head
for i in range(s-1):
    ptr = ptr.next
    ptr2 = ptr2.next
ptr = ptr.next
ptr2.next = ptr.next
ptr = None
return ptr3
