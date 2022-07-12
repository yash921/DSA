# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        find_length = 0
        temp = head
        while temp:
            find_length += 1
            temp = temp.next
        iter_ = find_length//k
        
        current, previous = head, None
        while iter_ > 0:
            
            last_node_of_previous_part = previous
            last_node_of_sub_list = current
            
            tempNode = None
            i = 0
            
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
            
            last_node_of_sub_list.next = current
            
            if current is None:
                break
            previous = last_node_of_sub_list
            iter_ -= 1
        return head
            
                
                
                
                
                
                
                
                
                
                
                
                
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        