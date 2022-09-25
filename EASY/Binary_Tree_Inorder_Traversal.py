ans = []


def Inorder(root):
    if not root:
        return None
    Inorder(root.left)
    ans.append(root.val)
    Inorder(root.right)


Inorder(root)
return ans
