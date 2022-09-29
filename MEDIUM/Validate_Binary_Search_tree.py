class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1, len(ans)):
            if ans[i-1] >= ans[i]:
                return False
        return True
