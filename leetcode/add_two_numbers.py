class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        added_val = l1.val + l2.val

        if l1.next or l2.next:
            if not l1.next:
                l1.next = ListNode()
            if not l2.next:
                l2.next = ListNode()

        if added_val >= 10:
            added_val %= 10
            if l1.next:
                l1.next.val += 1
            elif l2.next:
                l2.next.val += 1
            else:
                l1.next = ListNode(1)
                l2.next = ListNode()

        if l1.next or l2.next:
            return ListNode(added_val,
                            next=self.addTwoNumbers(l1.next, l2.next))
        else:
            return ListNode(added_val)


print(Solution().addTwoNumbers(
        ListNode(1, next=ListNode(8)),
        ListNode(0)
    ))
