# Example 1:

# Input: 2 -> 4 -> 6 ->  8 -> 10 -> 12 -> 7 -> null
# Output: 2 -> 7 -> 4 -> 12 -> 6 -> 10 -> 8 -> null 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrange(head):
    find_middle = middle(head)  # 8

    last_node = reverse(find_middle)
    temp = head
    # traverseSLL(last_node)
    # 2 -> 4 -> 6 ->  8   12 -> 10 -> 8 -> null
    while (temp is not None and last_node is not None):
        store = temp.next  # 8
        temp.next = last_node # 2 -> 12 -> 4 -> 10 -> 6 -> 8
        last_node = last_node.next # None
        temp.next.next = store  # 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> None
        temp = store  # 6
    
    if temp is not None:
        temp.next = None

    traverseSLL(head)

def traverseSLL(head):
    if head is None:
        print("Singly Linked List Is Empty!!")
    else:
        node = head
        while node is not None:
            print(node.value)
            node = node.next


def middle(head):
    slow = head
    fast = head

    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow
    
# 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
def reverse(head):
    prev = None
    current = head
    while current:
        tempNode = current.next # 12
        current.next = prev # 2 -> 4 -> 6 -> 8 -> None
        prev = current # 8
        current = tempNode # 10
    return prev


def main():
    obj = Node(2)
    obj.next = Node(4)
    obj.next.next = Node(6)
    obj.next.next.next = Node(8)
    obj.next.next.next.next = Node(10)
    obj.next.next.next.next.next = Node(12)
    obj.next.next.next.next.next.next = Node(7)

    rearrange(obj)

main()