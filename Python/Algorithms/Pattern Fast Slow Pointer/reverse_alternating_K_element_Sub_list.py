class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

def alternative(head, k):

    current, previous = head, None

    while True:

        last_node_of_previous_part = previous
        last_node_of_sub_part = current

        i = 0
        tempNode = None

        while current is not None and i < k:
            tempNode = current.next
            current.next = previous
            previous = current
            current = tempNode
            i += 1
        
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        last_node_of_sub_part.next = current
        
        
        
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1
        if current is None:
            break
    
    return traverseSLL(head)
    
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
    print(alternative(head, k))

main()