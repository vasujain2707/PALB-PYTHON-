QUES-Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and 
columns is always odd. Return the median of the matrix

import bisect

class Solution:
    def median(self, mat, r, c):
        
        # Minimum and maximum possible values
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        
        desired = (r * c) // 2
        
        while low <= high:
            mid = (low + high) // 2
            
            # Count elements <= mid
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
