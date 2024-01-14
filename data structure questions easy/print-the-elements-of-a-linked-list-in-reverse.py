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
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

def reversePrint(llist):
    # Base case: if the current node is None (end of the list), return https://www.youtube.com/watch?v=K7J3nCeRC80
    if not llist:
        return
    # Recursive call: move to the next node and call the function again in loop for llist not to always point at first element and llist.next to not always point to the second element you have to do something like llist=llist.next to move one by one over but that is not the case in recursion reversePrint(list.next) does move next one by one, and the print loc determines what order
    reversePrint(llist.next)
    # Print the data of the current node after returning from the recursive call
    print(llist.data)

# Example of a linked list: 1 -> 2 -> 3 -> 4
# llist points to the head of the linked list

# Calling the function with the linked list as an example:
# reversePrint(llist)
# This will be executed as follows:

# Initial call:
# reversePrint(1)
#   Recursive call: reversePrint(2)
#     Recursive call: reversePrint(3)
#       Recursive call: reversePrint(4)
#         Base case: return (4 is printed)
#       After returning from the recursive call, print(3)
#     After returning from the recursive call, print(2)
#   After returning from the recursive call, print(1)
# Finally, the output will be: 4 3 2 1

if __name__ == '__main__':
    tests = 1  # Assume one test case

    for tests_itr in range(tests):
        llist_count = 6  # Number of elements in the linked list

        llist = SinglyLinkedList()

        data_list = [3, 16, 13, 7, 1, 2]

        for llist_item in data_list:
            llist.insert_node(llist_item)

        # Reverse print the linked list
        reversePrint(llist.head)
