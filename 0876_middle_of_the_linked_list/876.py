from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        li = head

        while li != None:
            length += 1
            li = li.next

        for _ in range(int(length / 2)):
            head = head.next

        return head


if __name__ == "__main__":
    sol = Solution()

    query1 = ListNode(1)
    query2 = ListNode(2)
    query3 = ListNode(3)
    query4 = ListNode(4)
    query5 = ListNode(5)
    query6 = ListNode(6)
    query1.next = query2
    query2.next = query3
    query3.next = query4
    query4.next = query5
    query5.next = query6

    ans = sol.middleNode(query1)

    print(ans.val)


"""
Solution


Approach 1: Output to array

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]


Approach 2: Fast and Slow Pointer

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

"""
