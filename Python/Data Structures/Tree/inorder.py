class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOrderTraversalRecusive(root):

    arr = []

    def traversal(node):
        if node is None:
            return
        traversal(node.left)
        arr.append(node.value)
        traversal(node.right)
    traversal(root)
    return arr

def inOrderTraversalIterative(root):
    node = root
    stack = []
    result = []

    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            if not stack:
                break
            node = stack.pop()
            result.append(node.value)
            node = node.right
    return result



def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    print(inOrderTraversalRecusive(root)) 
    print(inOrderTraversalIterative(root)) 

    # inOrderTraversal = [7, 4, 8, 2, 5, 1, 3, 6]

"""
       1
      / \
     2   3
    / \   \
   4   5   6
  / \
 7   8
     
"""
    

main()