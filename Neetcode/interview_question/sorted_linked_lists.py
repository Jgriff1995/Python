from typing import List
import random


# Class for Nodes
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_node(self):
        print(self.val)


# Class for LinkedList and necessary operations
class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertAtEnd(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_node(self, val):
        current_node = self.head

        if current_node is not None and current_node.val == val:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next is not None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def print_Linked_list(self) -> str:
        current_node = self.head
        output = "["
        while current_node:
            output += str(current_node.val)
            if current_node.next:
                output += " -> "
            current_node = current_node.next
        output += "]"
        return output if output != "[]" else "[Empty list]"

    def size_of_Linked_list(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size


class Solution(object):
    # helper function to randomly generated n number of linked lists and insert them
    # into a list
    def initalize_linked_lists_into_list(self, n: int) -> List[LinkedList]:
        result = []

        for _ in range(n):
            # Create a new linked list
            current_list = LinkedList()
            # Generate a random length between 1 and 5 for this list
            length = random.randint(1, 5)
            # Start with a random number between 1 and 10
            current_val = random.randint(1, 10)

            # Generate sorted numbers for this list
            for _ in range(length):
                current_list.insertAtEnd(current_val)
                # Next number will be 1-5 more than current to maintain sorting
                current_val += random.randint(1, 5)

            result.append(current_list)

        return result

    # main function
    def sortedLinkedLists(self, input_list: List[LinkedList]) -> LinkedList:
        """
        Given a list of already sorted LinkedLists, return a singly sorted List
        """
        if not input_list:
            return LinkedList()

        # Initialize result linked list with dummy node
        result_linked_list = LinkedList()
        head = Node(self)
        result_linked_list.insertAtEnd(head)
        current = result_linked_list.head

        # Convert input lists to list of heads
        list_heads = [linked_list.head for linked_list in input_list]

        # Continue until all lists are exhausted
        while True:
            minimum_value = float("inf")
            minimum_index = -1

            # Find minimum value among all list heads
            for index, current_head in enumerate(list_heads):
                if current_head and current_head.val < minimum_value:
                    minimum_value = current_head.val
                    minimum_index = index

            # If no minimum found, all lists are exhausted
            if minimum_index == -1:
                break

            # Add minimum value to result and move corresponding list head
            current.next = list_heads[minimum_index]
            list_heads[minimum_index] = list_heads[minimum_index].next
            current = current.next

        # Remove dummy node
        result_linked_list.remove_first_node()

        return result_linked_list


if __name__ == "__main__":
    solution = Solution()
    list_of_linked_lists = solution.initalize_linked_lists_into_list(5)
    index = 0
    print("---------------------")
    print("Current Linked Lists:")
    print("---------------------")
    for temp in list_of_linked_lists:
        print(f"List: {index} : {temp.print_Linked_list()}")
        index += 1
    print()
    result = solution.sortedLinkedLists(list_of_linked_lists)
    print(f"Sorted List of Linked Lists:")
    print(f"{result.print_Linked_list()}")
