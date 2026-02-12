QUES- Given a collection of candidate numbers (candidates) and a target number (target), find 
all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates, target):
        
        candidates.sort()  # sort to handle duplicates
        result = []
        
        def backtrack(start, current, remaining):
            
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If number exceeds remaining, stop (because sorted)
                if candidates[i] > remaining:
                    break
                
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result
