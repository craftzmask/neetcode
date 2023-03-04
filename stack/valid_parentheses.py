class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(':')', 
            '{':'}',
            '[':']'
        }

        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            elif not stack:
                return False
            elif brackets[stack.pop()] != bracket:
                return False

        return not stack