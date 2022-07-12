class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preOrderTraversalRecusive(root):

    arr = []

    def traversal(node):
        if node is None:
            return
        arr.append(node.value)
        traversal(node.left)
        traversal(node.right)
    traversal(root)
    return arr

def preOrderTraversalIterative(root):
    node = root
    stack = [node]
    result = []

    while stack != []:
        node = stack.pop()
        result.append(node.value)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
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
    print(preOrderTraversalRecusive(root)) 
    print(preOrderTraversalIterative(root)) 

    # preOrderTraversal = [1,2,4,7,8,5,3,6]

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