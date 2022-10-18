class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        print(last)
        j = 0
        start = 0
        ans = []
        for i in range(len(s)):
            j = max(j, last[s[i]])
            if i == j:
                ans.append(i-start+1)
                start = i+1
        return ans
