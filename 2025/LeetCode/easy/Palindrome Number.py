"""Given an integer x, return true if x is a palindrome, and false otherwise."""
"""Follow up: Could you solve it without converting the integer to a string?"""


class Solution:

    @staticmethod
    def romanToInt(s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total, prev_value = 0, 0

        for char in reversed(s):
            curr_value = roman_values[char]

            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value

            prev_value = curr_value

        return total


assert Solution().romanToInt('MCMXCIV') == 1994