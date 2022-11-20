class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split()
        ans = []
        for i in s:
            if len(i) <= 2:
                ans.append(i.lower())
            else:
                s1 = ""
                if i[0].islower():
                    s1 += i[0].upper()
                    s1 += i[1:].lower()
                else:
                    s1 += i[0]+i[1:].lower()
                ans.append(s1)
        str1 = ""
        print(ans)
        for i in ans:
            str1 += i
            str1 += " "
        return str1.strip()
