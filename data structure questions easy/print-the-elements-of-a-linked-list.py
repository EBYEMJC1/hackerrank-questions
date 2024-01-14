class SinglyLinkedListNode:
    def __init__(self, node_data):
        # Initialize a new node with the given data
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        # Create a new node with the given data
        node = SinglyLinkedListNode(node_data)
        # Check if the linked list is empty
        if not self.head:
            # If empty, set the new node as both head and tail
            self.head = node
        else:
            # If not empty, set the new node as the next node of the tail the tail is the previous tail before adding the new node and so need to mke the next of the previous tail to the new tail
            self.tail.next = node
        # Update the tail to be the new node
        self.tail = node
        # Steps performed:
        # 1. Created a new node with the given data.
        # 2. Checked if the linked list is empty.
        # 3. If empty, set the new node as both head and tail.
        # 4. If not empty, set the new node as the next node of the tail.
        # 5. Updated the tail to be the new node.

    def print_linked_list(self):
        # Print the linked list starting from the head
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        # Steps performed:
        # 1. Set the current node to be the head of the linked list.
        # 2. While there is a current node:
        #    a. Print the data of the current node.
        #    b. Move to the next node.

if __name__ == '__main__':
    llist = SinglyLinkedList()
    data_list = [3, 16, 13, 7, 1, 2]
    # Adding nodes to the linked list one by one
    for llist_item in data_list:
        llist.insert_node(llist_item)
    # Printing the resulting linked list
    llist.print_linked_list()
