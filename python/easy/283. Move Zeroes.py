"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""


# My solutions
# Runtime: 128 ms, Beats 48.82%
# Memory Usage: 18.19 MB, Beats 16.01%
# O(N)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == 0:
                if nums[i] == nums[j]:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1


# Alternate solutions
# Runtime: 116 ms, Beats 93.76%
# Memory Usage: 18.04 MB, Beats 52.17%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
