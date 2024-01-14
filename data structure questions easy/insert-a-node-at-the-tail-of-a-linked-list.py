class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next
        if node:
            print(sep, end='')

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
    else:
        temp=head
        while temp:
            temp_minus_one = temp
            #stops when temp is null and so cannot assign temp to next node after for loop because there is no null.next so instead need the one right before it which is why whe have temp-one so can assign that node's next to new node after while loop
            temp=temp.next
        temp_minus_one.next = node     
    # Steps performed:
    # 1. Created a new node with the given data.
    # 2. Checked if the linked list is empty.
    # 3. If empty, set the new node as both head and tail.
    # 4. If not empty, traversed the linked list to find the tail.
    # 5. Saved the current node as the one before the tail.
    # 6. Set the new node as the next node after the tail.

    return head

if __name__ == '__main__':
    llist = SinglyLinkedList()
    data_list = [3, 16, 13, 7, 1, 2]
    # Adding nodes to the linked list one by one at the tail
    for item in data_list[:]:
        llist.head = insertNodeAtTail(llist.head, item)
    # Printing the resulting linked list
    print_singly_linked_list(llist.head, ' ')
