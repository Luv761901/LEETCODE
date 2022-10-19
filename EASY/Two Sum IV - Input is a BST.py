# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = []
        levelorder1 = []

        def levelorder(root):
            if root is None:
                return
            queue.append(root)
            while(len(queue) > 0):
                levelorder1.append(queue[0].val)
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        levelorder(root)
        if len(levelorder1) == 1:
            return False
        d = {}
        for i in range(len(levelorder1)):
            d[levelorder1[i]] = i
        print(d)

        for i in range(len(levelorder1)):
            x = k-levelorder1[i]
            if x in d and d[x] != i:
                return True
        return False
