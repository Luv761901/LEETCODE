class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        for i in items:
            if ruleKey == "type":
                if i[0] == ruleValue:
                    c += 1
            if ruleKey == "color":
                if i[1] == ruleValue:
                    c += 1
            if ruleKey == "name":
                if i[2] == ruleValue:
                    c += 1
        return c
