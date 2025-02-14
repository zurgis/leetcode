"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:

1 <= n <= 104
"""

# My solutions
# Runtime: 92 ms, faster than 19.72% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15 MB, less than 43.55% of Python3 online submissions for Fizz Buzz.
# Runtime O(n), Memory O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else 
            "Fizz" if i % 3 == 0 else 
            "Buzz" if i % 5 == 0 else 
            str(i) for i in range(1, n + 1)
        ]


# Runtime: 81 ms, faster than 40.59% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15.2 MB, less than 17.46% of Python3 online submissions for Fizz Buzz.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return list(map(self.replace, [i for i in range(1, n + 1)]))
    
    def replace(self, i):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return str(i)


# Runtime: 88 ms, faster than 27.19% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 14.9 MB, less than 85.41% of Python3 online submissions for Fizz Buzz.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ans list
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif divisible_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif divisible_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))

        return ans