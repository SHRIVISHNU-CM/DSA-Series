# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def diameter(self, root):
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the max diameter
            self.max_diameter = max(self.max_diameter, left_height + right_height + 1)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        height(root)
        return self.max_diameter

def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

if __name__ == "__main__":
    # Build the tree
    root = build_tree()

    # Create a Solution object
    solution = Solution()

    # Calculate and print the diameter
    print("Diameter of the tree:", solution.diameter(root))