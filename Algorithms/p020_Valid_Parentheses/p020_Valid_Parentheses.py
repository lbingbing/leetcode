class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack or \
                 c==')' and stack[-1]!='(' or \
                 c==']' and stack[-1]!='[' or \
                 c=='}' and stack[-1]!='{':
                return False
            else:
                stack.pop()
        return not stack
