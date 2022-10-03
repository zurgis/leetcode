"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


# My Solutions
# Runtime: 51 ms, faster than 94.57% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.2 MB, less than 53.01% of Python3 online submissions for Ransom Note.
# Runtime O(n), Memory O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        first = Counter(ransomNote)
        second = Counter(magazine)
        
        for i, j in first.items():
            if i not in magazine or second[i] < j:
                return False
            
        return True


# In one line
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
