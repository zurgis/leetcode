"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


# My solutions
# Runtime: 33 ms, Beats 69.58%
# Memory Usage: 13.8 MB, Beats 97.61%
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []

        for item in s:
            if item in pairs:
                stack.append(item)
            elif len(stack) == 0 or item != pairs[stack.pop()]:
                return False

        return len(stack) == 0


# Another solution (without stack)
# Runtime: 47 ms, Beats 24.67%
# Memory Usage: 13.9 MB, Beats 19.30%
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return False if len(s) != 0 else True
