class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pathWithGivenSequence(node, targetPath):
    return findPathWithGivenSequence(node, [], targetPath)

def findPathWithGivenSequence(currentNode, currentPath, targetPath):
    if currentNode is None:
        return False
    currentPath.append(currentNode.value)
    if currentPath == targetPath and currentNode.left is None and currentNode.right is None:
        return True
    left = findPathWithGivenSequence(currentNode.left, currentPath, targetPath)
    right = findPathWithGivenSequence(currentNode.right, currentPath, targetPath)
    del currentPath[-1]
    return left or right
    




def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)

    targetPath = [1,2,4,7]
    print(pathWithGivenSequence(root, targetPath)) 

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