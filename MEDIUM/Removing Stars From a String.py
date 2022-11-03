class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in range(len(s)-1, -1, -1):
            if ans == []:
                ans.append(s[i])
            elif ans[-1] == "*" and s[i] != "*":
                ans.pop()
            else:
                ans.append(s[i])
        print(ans)
        s = "".join(ans)
        return s[::-1]
