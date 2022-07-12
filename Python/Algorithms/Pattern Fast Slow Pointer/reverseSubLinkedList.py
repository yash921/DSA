class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head = [1,2,3,4,5], left = 2, right = 4 ---> 4 -> 3 -> 2
class Solution:
    def reverseBetween(self, head, left, right):
        # arr = []
        # temp = head
        
        # while temp:
        #     arr.append(temp.val)
        #     temp = temp.next
        
        # left = left-1
        # right = right-1
        
        # while left <= right:
        #     arr[left], arr[right] = arr[right], arr[left]
        #     left += 1
        #     right -= 1
            
        # newHead = None
        # newTail = None
        
        # for node in arr:
        #     newNode = ListNode(node)
        #     if newHead is None:
        #         newHead = newNode
        #         newTail = newNode
        #     else:
        #         newTail.next = newNode
        #         newTail = newNode
        return newHead
                