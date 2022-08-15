from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = iter = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                iter.next = list1
                list1 = list1.next
            else:
                iter.next = list2
                list2 = list2.next
            iter = iter.next

        if list1 or list2:
            iter.next = list1 if list1 else list2

        return head.next


if __name__ == "__main__":
    sol = Solution()

    list1_1 = ListNode(1)
    list1_2 = ListNode(2)
    list1_3 = ListNode(4)
    list1_1.next = list1_2
    list1_2.next = list1_3

    list2_1 = ListNode(1)
    list2_2 = ListNode(3)
    list2_3 = ListNode(4)
    list2_1.next = list2_2
    list2_2.next = list2_3

    ans = sol.mergeTwoLists(list1_1, list2_1)

    while ans:
        print(ans.val)
        ans = ans.next
