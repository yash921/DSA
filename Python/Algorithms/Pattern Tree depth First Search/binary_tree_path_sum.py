class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def treePathSum(node, targetVal):
    if node is None:
        return False
    
    if node.value == targetVal and node.left is None and node.right is None:
        return True
    
    return treePathSum(node.left, targetVal-node.value) or treePathSum(node.right, targetVal-node.value)


#Solution - 2
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def hasPathSum(self, node: Optional[TreeNode], targetVal: int) -> bool:
#         sums_ = []
#         self.calculateBranchSum(node, 0, sums_)
#         if targetVal in sums_:
#             return True
#         else:
#             return False
    
#     def calculateBranchSum(self, node, runningSum, sums_):
#         if node is None:
#             return
#         newRunningSum = runningSum + node.val
        
#         if node.left is None and node.right is None:
#            sums_.append(newRunningSum) 
#            return
#         self.calculateBranchSum(node.left, newRunningSum, sums_)
#         self.calculateBranchSum(node.right, newRunningSum, sums_)
          



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
    print(treePathSum(root, targetVal)) 

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