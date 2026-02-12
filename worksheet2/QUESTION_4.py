ques- Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] 
inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra 
space.

class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Detect cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find entrance of cycle
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
