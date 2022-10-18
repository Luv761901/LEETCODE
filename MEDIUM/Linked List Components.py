class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        curr = head
        res = 0
        flag = False

        while curr:
            if curr.val in nums:
                if not flag:
                    res += 1
                    flag = True
            else:
                flag = False
            curr = curr.next
        return res
