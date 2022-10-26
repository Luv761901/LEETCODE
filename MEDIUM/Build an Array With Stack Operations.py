class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = list(set(target))
        ans = []
        for i in range(1, t[-1]+1):
            ans.append("Push")
            if i not in t:
                ans.append("Pop")
        return ans
