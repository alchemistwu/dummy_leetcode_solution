# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        root = l1

        if l2 and l1.val >= l2.val:
            root = ListNode(l2.val, l1)
            l2 = l2.next

        tmp_root = root

        while (l2 and l1.val >= l2.val):
            tmp = ListNode(l2.val, l1)
            tmp_root.next = tmp
            tmp_root = tmp_root.next
            l2 = l2.next

        while (l2):
            if not l1.next:
                while (l2 and l2.val <= l1.val):
                    l1.next = ListNode(l1.val)
                    l1.val = l2.val
                    l1 = l1.next
                    l2 = l2.next

                if l2:
                    l1.next = l2
                break

            if l1.next.val > l2.val:
                tmp = ListNode(l2.val, l1.next)
                l1.next = tmp
                l2 = l2.next
            l1 = l1.next

        return root