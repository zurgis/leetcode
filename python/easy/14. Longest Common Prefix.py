"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

# My solutions
# Runtime: 36 ms, Beats 69.81%
# Memory Usage: 14 MB, Beats 42.18%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


# Best solutions
# Runtime: 33 ms, Beats 83.26%
# Memory Usage: 13.9 MB, Beats 82.50%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _lcp = ''

        for i, item in enumerate(zip(*strs)):
            if len(set(item)) != 1:
                break

            _lcp += item[0]

        return _lcp
