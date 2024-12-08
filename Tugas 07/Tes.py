class Solution(object):
    def combine(n, k):
        def backtrack(start, current, result):
            if len(current) == k:
                result.append(current[:])
                return
            
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current, result)
                current.pop()
        
        result = []
        backtrack(1, [], result)
        return result
    
n = int(input())
k = int(input())

solution = Solution.combine(n, k)
print(solution)