class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
def reversalLevelOrder(root):
    if not root:
        return []
    
    queue = Queue()
    queue.enqueue(root)
    stack = []
    
    while not queue.is_empty():
        node = queue.dequeue()
        stack.append(node.data)
        if node.right:
            queue.enqueue(node.right)
        if node.left:
            queue.enqueue(node.left)

    result =[]
    while stack:
        result.append(stack.pop())

    return result


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right  =Node(60)

res = reversalLevelOrder(root)
print(res)