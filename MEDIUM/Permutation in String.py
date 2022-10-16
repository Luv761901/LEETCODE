class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        ws = 0
        matched = 0
        for i in range(len(s1)):
            if(s1[i] in d):
                d[s1[i]] += 1
            else:
                d[s1[i]] = 1
        for we in range(len(s2)):
            cur = s2[we]
            if(cur in d):
                d[cur] -= 1
                if(d[cur] == 0):
                    matched += 1
            if(matched == len(d)):
                return(True)

            if(we >= len(s1)-1):
                l = s2[ws]
                ws += 1
                if(l in d):
                    if(d[l] == 0):
                        matched -= 1

                    d[l] += 1
