from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        if len(s) <= 1:
            return False
        
        #Example of ())
        for c in s: #O(n)
            if c in ['[', '(', '{']:
                stack.append(c)
            else: #if this is right
                # c is the right parathesis
                #Checking matching
                if stack:
                    left_char = stack.pop() # [, {. (
                else: 
                    return False
                
                if left_char == '[' and c != ']':
                    return False
                elif left_char == '(' and c!= ')':
                    return False
                elif left_char == '{' and c!= '}':
                    return False
        # after already pushing to stack, check
        if len(stack) != 0:
            return False
        return True
        