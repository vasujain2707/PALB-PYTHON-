QUES-ou are given an integer array arr[ ]. For every element in the array, your task is to 
determine its Previous Smaller Element (PSE).
The Previous Smaller Element (PSE) of an element x is the first element that appears to 
the left of x in the array and is strictly smaller than x.
Note: If no such element exists, assign -1 as the PSE for that position.

def previous_smaller_element(arr):
    stack = []
    result = []
    
    for num in arr:
        # Remove elements >= current number
        while stack and stack[-1] >= num:
            stack.pop()
        
        # If stack is empty → no smaller element
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        # Push current number into stack
        stack.append(num)
    
    return result


# Example
arr = [1, 6, 2]
print(previous_smaller_element(arr))
