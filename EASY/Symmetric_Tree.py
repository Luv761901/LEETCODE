def t(A, B):
       if A == None and B == None:
            return True
        elif A == None or B == None:
            return False
        elif A.val != B.val:
            return False
        else:
            x = t(A.left, B.right)
            y = t(A.right, B.left)
            return x and y

if root == None:
    return None
else:
    return t(root.left, root.right)
