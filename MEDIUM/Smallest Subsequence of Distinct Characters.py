class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        d = Counter(s)
        p = set()
        for i in range(len(s)):
            d[s[i]] -= 1
            if s[i] not in p:
                while len(stack) != 0 and stack[-1] > s[i] and d[stack[-1]]:
                    p.remove(stack[-1])
                    stack.pop()
                p.add(s[i])
                stack.append(s[i])
        return "".join(stack)
