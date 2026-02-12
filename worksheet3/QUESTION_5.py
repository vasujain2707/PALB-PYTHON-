QUES-Given an array arr[] of positive integers. Return true if all the array elements are 
palindrome otherwise, return false

class Solution:
    def PalinArray(self, arr):
        for num in arr:
            s = str(num)
            if s != s[::-1]:
                return False
        return True
