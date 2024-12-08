class Solution(object):
    def subsets(nums):
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

nums = [1, 2, 3]
subsets = Solution.subsets(nums)
print(subsets)
print({1,2,2,1,1})