class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def preorder(root, lst):
            if not root:
                return None
            if root.left == root.right:
                if sum(lst)+root.val == targetSum:
                    ans.append(lst+[root.val])
                return

            if root.left:
                preorder(root.left, lst+[root.val])
            if root.right:
                preorder(root.right, lst+[root.val])

        ans = []
        preorder(root, [])
        return ans
