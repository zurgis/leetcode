"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


# My solutions
# Runtime: 7440 ms, Beats 6.10%
# Memory Usage: 14.9 MB, Beats 92.46%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, first in enumerate(nums):
            for j, second in enumerate(nums):
                if j == i:
                    continue

                if first + second == target:
                    return [i, j]


# Alternate solutions
# Runtime: 64 ms, Beats 77.2%
# Memory Usage: 15.3 MB, Beats 18.82%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}

        for i, j in enumerate(nums):
            value = target - j

            if value in dict_:
                return [dict_[value], i]

            dict_[j] = i


# Runtime: 1003 ms, Beats 36.96%
# Memory Usage: 14.8 MB, Beats 92.46%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            value = target - nums[i]

            if value in nums and nums.index(value) != i:
                return [i, nums.index(target - nums[i])]