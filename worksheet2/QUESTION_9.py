QUES-Given two arrays a[] and b[], your task is to determine whether b[] is a subset 
of a[].

class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):
        from collections import Counter
        
        freq = Counter(a)
        
        for num in b:
            if freq[num] <= 0:
                return False
            freq[num] -= 1
        
        return True

    
    
    
    
