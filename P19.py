class Node:
    def __init__(self,val):
        self.right = None
        self.left = None
        self.data = val

class Solution:
    def search(self,root,x):
        if root is None or root.data ==x:
            return root
        
        if root.data <x:
            return self.search(root.right,x)
        
        return self.search(root.left,x)
def insert(root,key):
    if root is None:
        return Node(key)
    
    if key<root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def main():
    root1 = None
    root1 = insert(root1,2)
    root1 = insert(root1,81)
    root1 = insert(root1,42)
    root1 = insert(root1,87)
    root1 = insert(root1,66)
    root1 = insert(root1,90)
    root1 = insert(root1,45)

    solution = Solution()
    x1 =87
    result1 = solution.search(root1,x1)
    print(f"{x1} {"1" if result1 else "0"}")

if __name__ == "__main__":
    main()

    
    
    