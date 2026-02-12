ques - You are given an array arr[] of non-negative numbers. Each number tells you the maximum 
number of steps you can jump forward from that position.

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If only one element, no jump needed
        if n <= 1:
            return 0
        
        # If first element is 0, cannot move
        if arr[0] == 0:
            return -1
        
        maxReach = arr[0]
        steps = arr[0]
        jumps = 1
        
        for i in range(1, n):
            
            # If reached last index
            if i == n - 1:
                return jumps
            
            # Update maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step
            steps -= 1
            
            # If no more steps left
            if steps == 0:
                jumps += 1
                
                # If current index >= maxReach, cannot move forward
                if i >= maxReach:
                    return -1
                
                # Reinitialize steps
                steps = maxReach - i
        
        return -1
