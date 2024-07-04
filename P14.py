class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []
    
    res = []
    queue = [root]

    while queue:
        Node= queue.pop(0)

        res.append(Node.data)

        if Node.left:
            queue.append(Node.left)

        if Node.right:
            queue.append(Node.right)

    return res

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right  =Node(60)

res = levelOrder(root)
print(res)