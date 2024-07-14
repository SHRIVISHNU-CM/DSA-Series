class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def deleteNode(root,key):
    if not root:
        return root
    if key < root.data:
        root.left  = deleteNode(root.left,key)
    elif key > root.data:
        root.right = deleteNode(root.right,key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = deleteNode(root.right , temp.data)

    return root

def inorderTraversal(root):
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right) if root else[]

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

key = 3

new_root = deleteNode(root,key)

print(inorderTraversal(new_root))