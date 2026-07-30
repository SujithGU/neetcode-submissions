class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        for bracket in s:
            if bracket == '[' or bracket == '{' or bracket == '(':
                bracket_stack.append(bracket)
            elif bracket == '}' and len(bracket_stack)>0 and bracket_stack[-1]== '{':
                bracket_stack.pop()
            elif bracket == ']' and len(bracket_stack)>0 and bracket_stack[-1]== '[':
                bracket_stack.pop()
            elif bracket == ')' and len(bracket_stack)>0 and bracket_stack[-1]== '(':
                bracket_stack.pop()
            else:
                return False
        
        return len(bracket_stack)==0
