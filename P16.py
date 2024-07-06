class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def height (root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height,right_height) +1

root = Node(1)
root.right =Node(2)
root.left = Node(2)

print(height(root))
