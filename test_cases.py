import unittest
import io
from unittest.mock import patch
from index import Node, LinkedList, printElementsLinkedList, insertNodeTailLinkedList, deleteNodePosition, compareTwoLinkedLists


class TestPrintElementsLinkedList(unittest.TestCase):
    def test_print_elements_empty_list(self):
        # Test case for an empty linked list
        linked_list = LinkedList()
        self.assertIsNone(printElementsLinkedList(linked_list.head))

    def test_random_elements(self):
        # Test case for a linked list with random numbers
        elements = [10, 2, 3, 4, 4, 4, 4, 5]
        linked_list = create_linked_list(elements)

        # patch module is responsible to redirect the output to the buffer instead of the to the console(console will make it difficult to capture and verify)
        # "with" statement ensures that the patching is applied only within the indented block.
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printElementsLinkedList(linked_list)

        # The printed output from the printElementsLinkedList function is captured in mock_stdout.getvalue().
        # .strip() to remove any leading or trailing whitespace characters from the string
        printed_output = mock_stdout.getvalue().strip()
        expected_output = '\n'.join(map(str, elements))

        self.assertEqual(printed_output, expected_output)


class TestinsertNodeTailLinkedList(unittest.TestCase):
    def test_empty_list_empty_data(self):
        linked_list = LinkedList()
        # Linked List None and Data empty
        result_head = insertNodeTailLinkedList(None, None)
        self.assertIsNotNone(
            result_head, "Need to be equal to 0 because it will create a default Node as 0")
        self.assertEqual(
            result_head.data, 0, "Need to be equal to 0 because it will create a default Node as 0")

        # Linked List None and Data true
        result_head = insertNodeTailLinkedList(None, 200)
        self.assertIsNotNone(
            result_head, "Need to be equal to 0 because it will create a default Node as 0")
        self.assertEqual(result_head.data, 200,
                         "Need to be equal to 0 because it will create a default Node as 0")

        # Linked List true and Data None
        result_head = insertNodeTailLinkedList(linked_list.head, None)
        self.assertIsNotNone(
            result_head, "Need to be equal to 0 because it will create a default Node as 0")
        self.assertEqual(
            result_head.data, 0, "Need to be equal to 0 because it will create a default Node as 0")

    def test_non_empty_list_with_data(self):
        # Test case for a non-empty linked list and some data
        provide_data = 200
        elements = [1, 2, 3, 4, 5, 6, 7, 5, 4,
                    3, 2, 1, 2, 4, 5, 6, 7, 8, 6, 5, 4]
        linked_list = create_linked_list(elements)
        result_head = insertNodeTailLinkedList(linked_list, provide_data)
        self.assertIsNotNone(
            result_head, "Should not be None because we have linked list and data")

        current_node = result_head
        while current_node.next:
            current_node = current_node.next
        self.assertEqual(current_node.data, provide_data,
                         "New node at the tail should have the provided data.")
        self.assertIsNone(current_node.next,
                          "Next node after the new node should be None.")


class TestDeleteNodePosition(unittest.TestCase):
    def test_empty_llist(self):
        llist = LinkedList()

        validation = deleteNodePosition(llist.head, None)
        self.assertIsNone(
            validation, "Need to return None because we are giving head and position None")

        validation = deleteNodePosition(llist.head, 6)
        self.assertIsNone(
            validation, "Need to return None even if we are sending the Position")

    def test_list_with_nodes_same_value(self):
        position = 4
        elements = [1, 2, 3, 4, 5, 5, 5, 5, 5, 50, 53, 5, 5, 6, 7, 44]
        llist = create_linked_list(elements)
        validation = deleteNodePosition(llist, position)

        self.assertIsNotNone(
            validation, "Should not be None because we have linked list and position")

        current_node = validation
        counter = 0
        while current_node.next:
            if current_node.data == 5 and counter <= position:
                self.assertEqual(current_node.data, 5,
                                 "The Node was not deleted with the a list with Nodes with the same values at the position 4.")
            counter += 1
            current_node = current_node.next

    def test_with_position_out_range(self):
        position = 1000
        elements = [1, 2, 3, 4, 5]
        llist = create_linked_list(elements)
        validation = deleteNodePosition(llist, position)

        self.assertIsNotNone(
            validation, "Should not be None because we have linked list and position")

        current_node = validation
        while current_node.next:
            current_node = current_node.next

        self.assertEqual(
            current_node.data, 5, "Any data should be deleted from the llist because the position is out of the range")
        self.assertIsNone(
            current_node.next, "The next node need to be None as long any Node was deleted")


class TestCompareTwoLinkedLists(unittest.TestCase):
    def test_empty_lists(self):
        llist1 = LinkedList()
        llist2 = LinkedList()

        validation1 = compareTwoLinkedLists(llist1.head, llist2.head)
        self.assertIsNone(
            validation1, "Need to return None because both llist are empty")

        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        llist1 = create_linked_list(elements)
        validation2 = compareTwoLinkedLists(llist1, None)
        validation3 = compareTwoLinkedLists(None, llist1)

        self.assertIsNone(
            validation2, "Need to return None because one llist is empty")
        self.assertIsNone(
            validation3, "Need to return None because one llist is empty")

    def test_comparing_equal_lists(self):
        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        llist1 = create_linked_list(elements)
        llist2 = create_linked_list(elements)

        validation = compareTwoLinkedLists(llist1, llist2)

        self.assertEqual(
            validation, 1, "Need to return 1 because both lists are equal")
        self.assertIsNotNone(
            validation, "It cant be None because we are giving two valid linked lists")

    def test_comparing_different_lists(self):
        elements1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        elements2 = [1, 2, 3, 4, 5]
        llist1 = create_linked_list(elements1)
        llist2 = create_linked_list(elements2)

        validation = compareTwoLinkedLists(llist1, llist2)

        self.assertEqual(
            validation, 0, "Need to return 0 because both lists are different")
        self.assertIsNotNone(
            validation, "It cant be None because we are giving two valid linked lists")


def create_linked_list(elements):
    if not elements:
        return None

    # Create the head of the linked list
    head = Node(elements[0])
    current = head

    # Create nodes for the remaining elements
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next

    return head


def linked_list_to_list(llist):
    result = []
    current = llist

    while current:
        result.append(current.data)
        current = current.next

    return result


if __name__ == '__main__':
    unittest.main()
