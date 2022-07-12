class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def middle_ll(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    middle = slow

    return middle.value










def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    # head.next.next.next.next.next.next.next = head.next.next.next.next

    print(middle_ll(head))

main()