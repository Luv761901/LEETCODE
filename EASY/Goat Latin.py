class Solution:
    def toGoatLatin(self, s: str) -> str:
        p=s.split()
        for i in range(len(p)):
            if p[i][0]=='a' or p[i][0]=='e' or p[i][0]=='i' or p[i][0]=='o' or p[i][0]=='u' or p[i][0]=='A' or p[i][0]=='E' or p[i][0]=='I' or p[i][0]=='O' or p[i][0]=='U':
                p[i]=p[i]+'ma'+'a'*(i+1)
            else:
                p[i]=p[i][1:]+p[i][0]+'ma'+'a'*(i+1)
        return ' '.join(p)