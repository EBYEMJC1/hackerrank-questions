```python
#constraints if nothng in original return none if list length is less than n return whole list
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

def copy_first_n_nodes(head, n):
    if not head:
        return None
    
    dummy = Node(None, None)  # Dummy head for the copied list
    prev = dummy  # Pointer to keep track of the last node in the copied list remember you are copying addresses not values
    
    # Initialize head2 outside the loop
    head2 = None
    
    for _ in range(n):
        temp = Node(head.value, None)  # Create a new node for the copied list
        if head2 is None:  # Only set head2 once, after the loop
            head2 = temp
        prev.next = temp  # Link the new node to the previous one in the copied list
        prev = temp  # Update the previous pointer to the new node because the new node will become the previous node in the next iteration remember you are copying addresses not values
        head = head.next  # Move to the next node in the original list
        
        # Break the loop if we've reached the end of the list
        if not head:
            return head2
      ```
      
    return head2  # Return the head of the copied list



