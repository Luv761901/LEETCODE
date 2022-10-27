# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        temp = head
        count = 0
        while(ptr.next != None):
            ptr = ptr.next
            count += 1
        s = count+1
        for i in range(math.floor(s//2)):
            temp = temp.next
        return temp
