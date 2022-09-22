ptr = head
if head == None:
    return head
while(ptr.next != None):
    if ptr.val == ptr.next.val:
        ptr.next = ptr.next.next
    else:
        ptr = ptr.next
return head
