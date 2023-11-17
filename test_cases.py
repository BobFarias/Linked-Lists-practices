import unittest
import io
from unittest.mock import patch
from index import Node, LinkedList, printElementsLinkedList


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
