#1249. Minimum Remove to Make Valid Parentheses
#link :https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        parameters: 
            s: string
        return :
            string with the removed Parentheses  
        """
        stack = []
        lis = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    lis[i] = ''
        for i in stack:
            lis[i] = ''
        return "".join(lis)
        