from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            result.append(current[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        nums.sort()
        result = []
        backtrack(0, [])
        return result