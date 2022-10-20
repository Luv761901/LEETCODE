class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(-1)
            else:
                if stack[-1] == -1:
                    stack.pop()
                    stack.append(1)
                else:
                    S = 0
                    while stack[-1] != -1:
                        S += stack.pop()
                    stack.pop()
                    stack.append(2*S)
        return sum(stack)
