# def addTwoNumbers(l1, l2):
#     if len(l1) > len(l2):
#         small_list_node = l2
#         big_list_node = l1
#     else:
#         small_list_node = l1
#         big_list_node = l2

#     for count, val in enumerate(small_list_node):
#         index = count
#         big_list_node[count] = big_list_node[count] + val
#         while big_list_node[index] >= 10:
#             big_list_node[index] = big_list_node[index] % 10
#             if index + 1 > len(big_list_node) - 1:
#                 big_list_node.append(1)
#             else:
#                 big_list_node[index + 1] = big_list_node[index+1] + 1
#                 index += 1

#     return big_list_node


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # breakpoint()
        added_val = l1.val + l2.val

        if l1.next or l2.next:
            if not l1.next:
                l1.next = ListNode()
            if not l2.next:
                l2.next = ListNode()

        if added_val >= 10:
            added_val %= 10
            if l1.next or l2.next:
                if l1.next:
                    l1.next.val += 1
                elif l2.next:
                    l2.next.val += 1

                    
        if l1.next or l2.next:
            return ListNode(added_val, next=self.addTwoNumbers(l1.next, l2.next))
        else:
            return ListNode(added_val)


print(Solution().addTwoNumbers(
        ListNode(1, next=ListNode(8)),
        ListNode(0)
    ))