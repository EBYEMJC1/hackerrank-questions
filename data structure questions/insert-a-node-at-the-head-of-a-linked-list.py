class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next
        if node:
            print(sep, end='')

def insertNodeAtHead(llist, data):
    # Create a new node with the given data
    new_head = SinglyLinkedListNode(data)
    # Check if the linked list is not empty
    if llist:
        # Save the current head as the next node of the new head
        previous_head = llist
        # Set the new head as the head of the linked list
        llist = new_head
        llist.next = previous_head
    else:
        # If the linked list is empty, set the new node as both head and tail
        llist = new_head

    # Steps performed:
    # 1. Created a new node with the given data.
    # 2. Checked if the linked list is not empty.
    # 3. If not empty, saved the current head as the next node of the new head.
    # 4. Set the new head as the head of the linked list.
    # 5. If the linked list is empty, set the new node as both head and tail.

    return llist

if __name__ == '__main__':
    llist = SinglyLinkedList()
    data_list = [3, 16, 13, 7, 1, 2]
    # Adding nodes to the linked list one by one as the head
    for llist_item in data_list:
        llist.head = insertNodeAtHead(llist.head, llist_item)
    # Printing the resulting linked list
    print_singly_linked_list(llist.head, ' ')
