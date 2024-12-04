class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        output = list(s)
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    output[i] = ''
        
        #remove all ( from the end of string
        while stack:
            idx = stack.pop()
            print(idx)
            output[idx] = ''
        
        return ''.join(output)
        
            

        # o(len(s)) space complexity of how many paranthesis there are inside the string
