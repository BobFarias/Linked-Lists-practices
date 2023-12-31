import os


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


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

    # # Iterative method
    # if head is None:
    #     return head

    # while head:
    #     print(head.data)
    #     head = head.next


def insertNodeTailLinkedList(head, data):
    if head is None:
        new_node = Node(data or 0)
        return new_node

    #  Iterative mode
    #  current_node here is necessary:
    #  to preserve the reference to the original head of the linked list
    #  after the loop, head is still pointing to the first node.
    current_node = head

    while current_node.next:
        current_node = current_node.next

    current_node.next = Node(data)
    return head


def deleteNodePosition(head, position):
    if head is None or position is None:
        return head

    if position == 0:
        return head.next

    head.next = deleteNodePosition(head.next, position - 1)
    return head


def compareTwoLinkedLists(llist1, llist2):
    if llist1 is None or llist2 is None:
        return None

    equal_lists = 1

    while llist1:
        if llist1.data != llist2.data or llist2.next is None and llist1.next is not None:
            equal_lists = 0
            break

        llist1 = llist1.next
        llist2 = llist2.next

    return equal_lists


def getNodeSpecificPositionFromTail(llist, positionFromTail):
    if llist is None or positionFromTail is None:
        return llist

    pointer_node = llist

    while llist.next:
        llist = llist.next

        if positionFromTail == 0:
            pointer_node = pointer_node.next
        else:
            positionFromTail -= 1

    if positionFromTail > 0:
        return None

    return pointer_node.data


def insertNodeAtPosition(llist, data, position):
    if data is None or position is None or llist is None:
        return None

    if llist.next is None:
        return llist

    if position == 1:
        new_node = Node(data)
        new_node.next = llist.next
        llist.next = new_node
        return llist

    llist.next = insertNodeAtPosition(llist.next, data, position - 1)

    return llist


def mergeTwoSortedLinkedLists(head1, head2):
    if head1 is None and head2 is None:
        return None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    current_node = None
    if head1.data < head2.data:
        current_node = head1
        current_node.next = mergeTwoSortedLinkedLists(head1.next, head2)
    else:
        current_node = head2
        current_node.next = mergeTwoSortedLinkedLists(head1, head2.next)

    return current_node


# First Usage of the implementation:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list2 = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    linked_list2.append(1)
    linked_list2.append(2)
    linked_list2.append(3)
    linked_list2.append(5)
    linked_list2.append(9)

    # printElementsLinkedList(linked_list.head)
    # insertNodeTailLinkedList(linked_list.head, 200)
    # deleteNodePosition(linked_list.head, 2)
    # compareTwoLinkedLists(linked_list.head, linked_list2.head)
    # getNodeSpecificPositionFromTail(linked_list.head, 2)
    insertNodeAtPosition(linked_list.head, 50, 2)
