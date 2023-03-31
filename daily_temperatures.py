class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #empty 
        if len(temperatures) == 0:
            return []
        
        if len(temperatures) == 1:
            return [0]
        
        ans = []
        # ----------O(n^2)--------------
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    found = True
                    break
            # if not found
            if not found:
                ans.append(0)

        # ----------Stack------------
        # [90, 60, 30, 10, 100]
        # if temp <= i:
            #
                
        return ans
        
        