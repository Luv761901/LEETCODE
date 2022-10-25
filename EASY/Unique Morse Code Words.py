class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        a=[]
        for i in words:
            ans=""
            for j in i:
                ans+=d[j]
            a.append(ans)
        return len(set(a))    