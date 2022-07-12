class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sumNumbers(root):
    return calculateSum(root, 0)
        
    
def calculateSum(node, pathSum):
    if node is None:
        return 0
        
    pathSum = pathSum * 10 + node.value
    if node.left is None and node.right is None:
        return pathSum
        
    return calculateSum(node.left, pathSum) + calculateSum(node.right, pathSum)
        




def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)

    print(sumNumbers(root)) 

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