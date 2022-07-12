class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def alltreePathSum(node, targetVal):
    sums_ = []
    calculateBranchPath(node, [], sums_, targetVal)
    return sums_

def calculateBranchPath(node, currentPath, sums_, targetVal):
    if node is None:
        return 

    currentPath.append(node.value)

    if node.value == targetVal and node.left is None and node.right is None:
        sums_.append(list(currentPath))
    
    calculateBranchPath(node.left, currentPath, sums_, targetVal-node.value)
    calculateBranchPath(node.right, currentPath, sums_, targetVal-node.value)
    del currentPath[-1]




def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)

    targetVal = 10
    print(alltreePathSum(root, targetVal)) 

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