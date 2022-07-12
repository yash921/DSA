class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

def rotateALinkedList(head, k):
    if head is None or head.next is None:
        return head
    find_length = 0
    temp = head

    while temp:
        find_length += 1
        temp = temp.next
        
    rotate_ = k%find_length
    if rotate_ == 0:
        return head
    
    first_node = head
    current = head
    previous = None
    i = 0
    while current is not None and i < find_length - rotate_: # 0 < 3
        previous = current
        current = current.next
        i += 1

    previous.next = None
    newHead = current
        
    while current.next is not None:
        current = current.next

    current.next = first_node

    return newHead
        
    
    
def traverseSLL(head):
    if head is None:
        print("Singly Linked List Is Empty!!")
    else:
        node = head
        while node is not None:
            print(node.value)
            node = node.next


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    

    k = 2
    print(rotateALinkedList(head, k))

main()