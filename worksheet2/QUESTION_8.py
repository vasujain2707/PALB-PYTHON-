QUES-Given an integer n, find its factorial. Return a list of integers denoting the digits 
that make up the factorial of n

class Solution:
    def factorial(self, n):
        result = [1]  # Store digits
        
        for x in range(2, n + 1):
            carry = 0
            
            for i in range(len(result)):
                prod = result[i] * x + carry
                result[i] = prod % 10
                carry = prod // 10
            
            # Handle remaining carry
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        # Digits are stored in reverse order
        return result[::-1]
