class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        close_to_open = {'}':'{',']':'[',')':'('}

        for bracket in s:
            if bracket in close_to_open:
                # close bracket
                if bracket_stack and bracket_stack[-1]==close_to_open[bracket]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(bracket)
        
        return len(bracket_stack)==0
