class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None
        arr = []
        while(head != None):
            arr.append(head.val)
            head = head.next

        print(arr)

        def maketree(left, right):
            if left > right:
                return
            else:
                mid = (left+right)//2
                Node = TreeNode(arr[mid])
                Node.left = maketree(left, mid-1)
                Node.right = maketree(mid+1, right)
                return Node
        return maketree(0, len(arr)-1)
