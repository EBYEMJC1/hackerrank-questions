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

def print_singly_linked_list(node, sep=' '):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')

def reverse(llist):
    # https://youtu.be/sYcOK51hl-A?si=w85hJL_S3rff0NTw
    # https://www.youtube.com/watch?v=KYH83T4q6Vs
    # https://www.cs.usfca.edu/~galles/visualization/RecReverse.html
    if not llist.next:
        return llist
    head = reverse(llist.next)
    left_node = llist
    right_node = left_node.next
    right_node.next = left_node
    left_node.next = None

    # Steps performed:
    # 1. Set left_node to the current node.
    # 2. Set right_node to the next node.
    # 3. Set the next pointer of right_node to left_node, reversing the direction.
    # 4. Set the next pointer of left_node to None, disconnecting it 
    # Return the new head of the reversed list
    # 5. Repeat the process for each pair of nodes as the recursion unwinds.
    
    return head



    # example
    # list = 1->2->3->None

    # call 1.
    #     def reverse(llist)
    #         llist = 1->2->3->None
    #         stack for call 1 function = 1->2->3->None
    #     if not llist.next is false do not enter if

    # call 2.
    #     head = reverse(llist.next)
    #         llist = 2->3->None
    #         stack for call 2 function = 2->3->None
    #     if not llist.next is false do not enter if

    # call 3.
    #     head = reverse(llist.next)
    #         llist = 3->None
    #         stack for call 2 function = 3->None
    #     if not llist.next is True enter if
    #         return llist to whtever called it which was call 2 calling call 3 so return node that has 3->None in it to call 2 we will call this call 2'
    #         stack for call 3 is emptied

    # call 2':
    #     from call 2 
    #         llist = 2->3->None
    #     head = returned value from call 3 
    #         head = 3->None 
    #     left_node = llist
    #         left_node = 2->3->None
    #     right_node = left_node.next
    #         right node = 3->None
    #     right_node.next = left_node
    #         right_node.next or 3-> = left node or 2->3->None which makes 3->2->3->None
    #     left_node.next = None
    #         left_node.next or 2-> = None makind  3->2->None 
    #         head is now equal to 3->2->None since added 2 and none to it in this return and removed ->3->None
    #     return head to what called it which was call 1 so return 3->2->None to call 1 we will call this call 1' and stack for call 2 is emptied

    # call 1':
    #     from call 1 
    #         llist = 1->2->3->None
    #     head = returned value from call 2' 
    #         head = 3->2->None 
    #     left_node = llist
    #         left_node = 1->2->3->None
    #     right_node = left_node.next
    #         right node = 2->3->None
    #     right_node.next = left_node
    #         right_node.next or 2-> = left node or 1->2->3->None making 3->2->1->2->3->None
    #     left_node.next = None
    #         left_node.next or 1-> = None making 3->2->1->None 
    #         head is now equal to 3->2->1->None since added 1 and none to it in this return and removed ->2->3->None
    #     return head to what called it which was main so 3->2->1->None is returned to main and it does with it what it wants and stack for call 1 is emptied


if __name__ == '__main__':
    tests = 1  # Assume one test case
    for tests_itr in range(tests):
        llist_count = 6  # Number of elements in the linked list
        llist = SinglyLinkedList()
        data_list = [3, 16, 13, 7, 1, 2]
        for llist_item in data_list:
            llist.insert_node(llist_item)
        # Reverse the linked list
        llist1 = reverse(llist.head)
        # Print the resulting reversed linked list
        print_singly_linked_list(llist1, ' ')
