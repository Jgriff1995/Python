# Date: 3/03/2025
# Author: @Jgriff1995
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Time Spent: 1hr

class ListNode(object):
    """
    Definition for singly-linked list node.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    Merges two sorted linked lists into one sorted linked list.

    :type list1: Optional[ListNode] - The head of the first sorted linked list.
    :type list2: Optional[ListNode] - The head of the second sorted linked list.
    :rtype: Optional[ListNode] - The head of the merged sorted linked list.

    Time Complexity: O(n + m) - Where n and m are the lengths of list1 and list2, respectively.
    Space Complexity: O(1) - Constant space, as only a few pointers are used.
    """

    # Create a dummy node to serve as the head of the merged list.
    head = ListNode()
    current = head  # Pointer to build the merged list.

    # Traverse both lists and merge them in sorted order.
    while list1 and list2:  # While both lists are not empty.
        if list1.val < list2.val:  # If the current node in list1 is smaller.
            # Append list1's current node to the merged list.
            current.next = list1
            list1 = list1.next  # Move to the next node in list1.
        else:
            # Append list2's current node to the merged list.
            current.next = list2
            list2 = list2.next  # Move to the next node in list2.
        current = current.next  # Move the current pointer forward.

    # If one of the lists is not empty, append the remaining nodes.
    current.next = list1 or list2

    # Return the head of the merged list (skipping the dummy node).
    return head.next


# Helper function to convert a list to a linked list.
def list_to_linked_list(list):
    dummy = ListNode()
    current = dummy
    for val in list:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to convert a linked list to a list.
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test cases to validate the function.
print("Test Case 1: [1, 2, 4] and [1, 3, 4]: ", linked_list_to_list(mergeTwoLists(list_to_linked_list(
    [1, 2, 4]), list_to_linked_list([1, 3, 4]))))  # Output: [1, 1, 2, 3, 4, 4]
print("Test Case 2: [] and []: ", linked_list_to_list(mergeTwoLists(
    list_to_linked_list([]), list_to_linked_list([]))))  # Output: []
print("Test Case 3: [] and [0]: ", linked_list_to_list(mergeTwoLists(
    list_to_linked_list([]), list_to_linked_list([0]))))  # Output: [0]
print("Test Case 4: [1, 3, 5] and [2, 4, 6]: ", linked_list_to_list(mergeTwoLists(list_to_linked_list(
    [1, 3, 5]), list_to_linked_list([2, 4, 6]))))  # Output: [1, 2, 3, 4, 5, 6]
print("Test Case 5: [0] and [0]: ", linked_list_to_list(mergeTwoLists(
    list_to_linked_list([0]), list_to_linked_list([0]))))  # Output: [0, 0]
