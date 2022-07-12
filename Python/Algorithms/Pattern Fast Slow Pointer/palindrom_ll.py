class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

def is_palindrom(head):
    slow = head
    fast = head
        
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    middle = slow

    head_second_half = reverse(middle) #4
    
    copy_head_second_half = head_second_half
   

    while (head is not None and head_second_half is not None):
        if head.value != head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next
    
    reverse(copy_head_second_half)
    store = head
    traverseSLL(store)
    if head is None or head_second_half is None:
        return True
    return False

def reverse(head):
    current = head # 3
    prev = None  # 2 -> 3 -> 4 -> None

    while current:
        tempNode = current.next 
        current.next = prev
        prev = current
        current = tempNode
    return prev

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
    


    print(is_palindrom(head))

main()