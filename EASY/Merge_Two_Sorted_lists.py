a = []
if list1 == None and list2 == None:
    return list1
elif list1 == None:
    return list2
elif list2 == None:
    return list1

while(list1.next != None):
    a.append(list1.val)
    list1 = list1.next
a.append(list1.val)
while(list2.next != None):
    a.append(list2.val)
    list2 = list2.next
a.append(list2.val)
a.sort()
head = ListNode()
node = head
for i in a:
    node.next = ListNode(i)
    node = node.next
head = head.next
return head
