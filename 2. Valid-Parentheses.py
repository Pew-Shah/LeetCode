"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

class Solution:
    def isValid(self, s):
        if len(s) % 2 !=0:
            return False
    
        stack = []
        brackets = { '(':')' , '{':'}' , '[':']'}
        for i in s:
            if i in brackets:
                stack.append(i)
            else :
                if not stack:
                    return False
                a= stack.pop()
                if i !=brackets[a]:
                    return False
        return not stack

sol= Solution()
s = "{[()]}"
print(sol.isValid(s))