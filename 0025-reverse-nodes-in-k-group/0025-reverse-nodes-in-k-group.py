# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)  # Create a dummy node
        dummy.next = head  # Point dummy to the original head
        prev = dummy  # prev starts as the dummy node
        curr = head

        while curr:  # While there are still nodes to process
            kth_node = self.getkthNode(curr, k)  # Find the kth node in the current group
            print("kth node :", kth_node)

            if not kth_node:  # If there are fewer than k nodes left
                if prev:
                    prev.next = curr  # Connect the last group as is
                break  # Exit the loop as no more full groups can be reversed

            next_node = kth_node.next  # Save the node after kth node
            kth_node.next = None  # Temporarily break the list to reverse the group

            self.reverse_k_nodes(curr)  # Reverse the nodes in the current group

            # Check if this is the first group of reversal
            if curr == head:
                head = kth_node  # Update head to the new head of the reversed group
                dummy.next = head
                print("head", head)
            else:
                prev.next = kth_node  # Link the previous group to the new reversed group
                print("prev.next", prev.next)

            prev = curr  # Move prev to the current node
            print("prev:", prev)
            curr = next_node  # Move curr to the next node after the kth node
            print("curr:", curr)

        return dummy.next  # Return the new head after all groups are reversed

    def getkthNode(self, curr, k):  # curr advances to kth node if k=2
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr  # If no kth node, this will return None

    def reverse_k_nodes(self, curr):
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
