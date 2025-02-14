"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

# My solutions
# Runtime: 51 ms, Beats 95.7%
# Memory Usage: 13.8 MB, Beats 95.10%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# Alternate solutions (without string)
# Runtime: 60 ms, Beats 78.25%
# Memory Usage: 13.9 MB, Beats 51.94%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        value = 0
        while x > value:
            value = value * 10 + x % 10
            x //= 10
        
        return value == x or value // 10 == x