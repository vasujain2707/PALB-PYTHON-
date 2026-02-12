QUES-Given an array arr[] with non-negative integers representing the height of blocks. 
If the width of each block is 1, compute how much water can be trapped between 
the blocks during the rainy season.

class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left = 0
        right = n - 1
        
        leftMax = 0
        rightMax = 0
        water = 0
        
        while left <= right:
            
            if arr[left] <= arr[right]:
                if arr[left] >= leftMax:
                    leftMax = arr[left]
                else:
                    water += leftMax - arr[left]
                left += 1
            
            else:
                if arr[right] >= rightMax:
                    rightMax = arr[right]
                else:
                    water += rightMax - arr[right]
                right -= 1
        
        return water
