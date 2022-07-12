from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    #   1
#     /  \
#    2    3
#   / \  / \
#  4   5 6  7  
def tree_level_order_traversal(node):
    result = []
    if node is None:
        return 
    queue = deque()
    queue.append(node)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()

            currentLevel.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(currentLevel)
    return result

    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print(tree_level_order_traversal(root))

main()