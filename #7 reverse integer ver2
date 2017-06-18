class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #Convert to string
        n_to_string = str(x)[::-1]
        
        # Determine sign
        if x**3 != abs(x**3):
            negative = True
        else:
            negative = False
        
        
        result = 0
        # Use in-built reverse solution
        if not negative:
            result =  int(n_to_string)
        else:
            result = int(n_to_string[0:-1]) * -1
            
        # Check for overflow
        if abs(result) < 2**31:
            return result
        else:
            return 0
