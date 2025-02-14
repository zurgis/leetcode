"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# My Solutions
# Runtime: 33 ms, faster than 91.84% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 55.16% of Python3 online submissions for Middle of the Linked List.
# Runtime O(n), Memory O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        
        while head is not None:
            values.append(head)
            
            head = head.next
            
        return values[len(values) // 2:len(values) // 2 + 1].pop()


# Runtime: 30 ms, faster than 95.77% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 55.16% of Python3 online submissions for Middle of the Linked List.
# Runtime O(n), Memory O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
            slow = fast = head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
