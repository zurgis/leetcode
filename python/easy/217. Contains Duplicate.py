"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


# My solutions
# Runtime: 480 ms, Beats 5.10%
# Memory Usage: 34.51 MB, Beats 15.14%
# O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _dict = {}

        for i in nums:
            if _dict.get(i): 
                return True

            _dict[i] = 1


# Alternate solutions
# Runtime: 428 ms, Beats 24.73%
# Memory Usage: 31.96 MB, Beats 46.90%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
