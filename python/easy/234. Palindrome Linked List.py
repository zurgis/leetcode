"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# My solutions
# Runtime: 1807 ms, faster than 15.98% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.7 MB, less than 46.22% of Python3 online submissions for Palindrome Linked List.
# Runtime O(n), Memory O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        items = []
        
        while tmp is not None:
            items.append(tmp.val)
            tmp = tmp.next
            
        while head is not None:
            item = items.pop()
            
            if item != head.val:
                return False
            else:
                head = head.next
                
        return True


# Runtime: 2000 ms, faster than 9.17% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.5 MB, less than 62.06% of Python3 online submissions for Palindrome Linked List.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        items = []
        
        while head:
            items.append(head.val)
            head = head.next
            
        return items == items[::-1]


# Best Solution
# Runtime: 1075 ms, faster than 72.16% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 31 MB, less than 98.51% of Python3 online submissions for Palindrome Linked List.
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev


# Recursion
# Runtime: 1890 ms, faster than 12.87% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 128.4 MB, less than 5.00% of Python3 online submissions for Palindrome Linked List.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


# Reverse second half
# Runtime: 960 ms, faster than 81.11% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.8 MB, less than 29.18% of Python3 online submissions for Palindrome Linked List.
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous