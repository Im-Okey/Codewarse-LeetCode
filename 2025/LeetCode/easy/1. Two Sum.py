"""Given an array of integers nums and an integer target,
   return indices of the two numbers such that they add up to target.

 You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order."""
from typing import List


class Solution:

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        result = {}
        for index, i in enumerate(nums):
            if target - i in result.keys():
                return [result[target - i], index]
            else:
                result[i] = index
        return result


assert Solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
