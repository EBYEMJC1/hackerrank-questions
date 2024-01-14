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

def deleteNode(llist, position):
    if position == 0:
        # If the node to be deleted is the head, update the head to be the next node
        llist = llist.next
        return llist #if this is not here and all just return llist at bottom, it fails test 2 unsure as to why I DO NOT UNDERSTAND WHY RETURN HERE NEED TWO RETURNS AND NOT JUST ONE

    node_to_be_deleted = llist
    for i in range(position):
        # Traverse to the node to be deleted
        node_before_node_to_be_deleted = node_to_be_deleted
        node_to_be_deleted = node_to_be_deleted.next
    # Check if there is a next node
    if node_to_be_deleted.next:
        # If yes, update the next of the node before the node to be deleted to be the next of the node that is deleted
        node_before_node_to_be_deleted.next = node_to_be_deleted.next
    else:
        # If no next node, set the next of the node before to be None
        node_before_node_to_be_deleted.next = None

    # Steps performed:
    # 1. If the node to be deleted is the head, update the head to be the next node.
    # 2. Traverse to the node to be deleted.
    # 3. Check if there is a next node.
    #    a. If yes, update the next of the node before the node to be deleted.
    #    b. If no next node, set the next of the node before to be None.

    return llist

if __name__ == '__main__':
    llist = SinglyLinkedList()
    data_list = [3, 16, 13, 7, 1, 2]
    # Adding nodes to the linked list one by one
    for llist_item in data_list:
        llist.insert_node(llist_item)
    position = 2
    # Deleting a node at the specified position
    llist = deleteNode(llist.head, position)
    # Printing the resulting linked list
    print_singly_linked_list(llist, ' ')
