class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        #  Defining the new_node receiving the data from the parameter
        #  data mostly is an init
        new_node = Node(data)

        # If the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Finding the last node so it could be appened
        # the new node on the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    # Printing your current linked list
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def printElementsLinkedList(head):
    # Recursion method
    if head is None:
        return head
    print(head.data)
    printElementsLinkedList(head.next)

    # Iterative method
    if head is None:
        return head

    while head:
        print(head.data)
        head = head.next


# First Usage of the implementation:
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    printElementsLinkedList(linked_list.head)
