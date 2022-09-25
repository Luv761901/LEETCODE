a, b = [], []
if p == None and q != None:
    return False
elif p != None and q == None:
    return False


def traversal(c, head):
    if head == None:
        c.append('null')
    else:
        traversal(c, head.left)
        traversal(c, head.right)
        c.append(head.val)


traversal(a, p)
traversal(b, q)
if a == b:
    return True
else:
    return False
