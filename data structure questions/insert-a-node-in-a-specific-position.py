class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next
        if node:
            print(sep, end='')

def insertNodeAtPosition(llist, data, position):
    # Initialize a variable to keep track of the current node in the linked list.
    current_node = llist
    # Traverse the linked list to reach the node at the specified position.
    for i in range(position):
        # Keep track of the node before the current position.
        node_before_position = current_node
        # Move to the next node in the linked list, which will eventually hold the node that will be replaced.
        current_node = current_node.next
    # Create a new node with the given data.
    new_node = SinglyLinkedListNode(data)
    # Make the node before the current position point to the new node.
    node_before_position.next = new_node
    # Make the new node point to the node that was previously at the specified position.
    new_node.next = current_node
    
    # the steps taken to insert the new node at the specified position.
    # The node before the current position is updated to point to the new node,
    # and the new node is connected to the node that was previously at the specified position.

    # Return the modified linked list.
    return llist



if __name__ == '__main__':
    llist = SinglyLinkedList()
    data_list = [3, 16, 13, 7, 1, 2]

    for item in data_list[:-2]:
        llist.insert_node(item)

    data = data_list[-2]
    position = data_list[-1]

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ')
