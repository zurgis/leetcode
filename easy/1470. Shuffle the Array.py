"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
"""

# My solutions
# Runtime: 53 ms, Beats 97.74%
# Memory Usage: 14.1 MB, Beats 86.30%
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]
        result = []

        for i in range(n):
            result.append(first_half[i])
            result.append(second_half[i])

        return result


# Alternate solutions
# Runtime: 61 ms, Beats 79.49%
# Memory Usage: 14 MB, Beats 99.61%
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for nums in zip(nums[:n], nums[n:]) for num in nums]


# Best solutions
# Runtime: 63 ms, Beats 70.68%
# Memory Usage: 14.1 MB, Beats 86.30%
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])

        return result