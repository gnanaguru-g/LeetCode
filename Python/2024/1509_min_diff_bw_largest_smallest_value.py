from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(
            nums[-1] - nums[3],
            nums[-4] - nums[0],
            nums[-3] - nums[1],
            nums[-2] - nums[2]

        )
    
###
sol = Solution()
nums = [1,5,0,10,14]
print(sol.minDifference(nums))

'''Minimum Difference Between Largest and Smallest Value in Three Moves
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.'''
        