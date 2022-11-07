class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for j in words:
                if i == j:
                    continue
                else:
                    if i in j:
                        ans.append(i)
                        break

        return ans
