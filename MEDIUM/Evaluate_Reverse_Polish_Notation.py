class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = {'+': 0, '-': 0, '/': 0, '*': 0}
        for i in tokens:
            if i not in d:
                stack.append(i)
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(int(b) + int(a))
                elif i == "-":
                    stack.append(int(b) - int(a))
                elif i == "*":
                    stack.append(int(b) * int(a))
                else:
                    stack.append(int(int(b) / int(a)))
        return stack[0]
