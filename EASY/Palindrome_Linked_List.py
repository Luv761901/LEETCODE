class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        while(head.next != None):
            a.append(head.val)
            head = head.next
        a.append(head.val)
        if a == a[::-1]:
            return True
        else:
            return False
