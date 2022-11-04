# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a=[]
        while(head.next!=None):
            a.append(head.val)
            head=head.next
        a.append(head.val)
        print(a)
        s=""
        for i in a:
            s+=str(i)
        p=int(s,2)
        return p