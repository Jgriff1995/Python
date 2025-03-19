from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """ """
    print("We made it")
    result_1 = ""
    result_2 = ""

    current = l1
    while current.next is not None:
        result_1 += current.val
        current = current.next

    current = l2
    while current.next is not None:
        result_2 += current.val
        current = current.next

    # _sum = int(result_1) + int(result_2)
    print(result_1)
    print(result_2)
    return

list_1 = []

list_1.append(ListNode(2))
list_1.append(ListNode(4))
list_1.append(ListNode(3))

list_2 = []

list_2.append(ListNode(5))
list_2.append(ListNode(6))
list_2.append(ListNode(4))

head1 = list_1[0]
head2 = list_2[0]

current = head1

while current.next is not None:
    print(current.val)
    current = current.next

addTwoNumbers(head1, head2)
