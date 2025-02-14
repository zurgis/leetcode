/*
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
*/


// My solutions
// Runtime: 0 ms, Beats 100.00%
// Memory Usage: 2.30 MB, Beats 76.64%
func longestCommonPrefix(strs []string) string {
    prefix := strs[0]

    for _, value := range strs[1:] {
        for !strings.HasPrefix(value, prefix) {
            prefix = prefix[:len(prefix)-1]
        }
    }

    return prefix
}
