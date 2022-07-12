class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postOrderTraversalRecusive(root):

    arr = []

    def traversal(node):
        if node is None:
            return
        traversal(node.left)
        traversal(node.right)
        arr.append(node.value)
    traversal(root)
    return arr

def postOrderTraversalIterativeUsingTwoStacks(root):
    node = root
    s1 = [root]
    s2 = []
    result = []

    while s1 != []:
        node = s1.pop()
        s2.append(node)

        if node.left is not None:
            s1.append(node.left)
        if node.right is not None:
            s1.append(node.right)
    
    while s2 != []:
        node = s2.pop()
        result.append(node.value)
    
    return result
    

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
    print(postOrderTraversalRecusive(root)) 
    print(postOrderTraversalIterativeUsingTwoStacks(root)) 

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